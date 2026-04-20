from pathlib import Path

import duckdb
import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "warehouse" / "healthcare.duckdb"


@st.cache_resource
def get_connection():
    return duckdb.connect(str(DB_PATH), read_only=True)


@st.cache_data
def load_claims():
    query = """
    select
        claim_id,
        patient_id,
        provider_id,
        provider_name,
        specialty,
        organization_id,
        organization_name,
        patient_city,
        patient_state,
        try_cast(service_date as date) as service_date,
        status_primary,
        status_secondary,
        status_patient,
        coalesce(claim_outstanding_total, 0) as claim_outstanding_total,
        coalesce(latest_outstanding, 0) as latest_outstanding,
        coalesce(transaction_count, 0) as transaction_count,
        coalesce(total_transaction_amount, 0) as total_transaction_amount,
        coalesce(total_payments, 0) as total_payments,
        coalesce(total_adjustments, 0) as total_adjustments,
        coalesce(total_transfers, 0) as total_transfers,
        first_transaction_date,
        last_transaction_date,
        financial_priority_bucket
    from int_claim_enriched
    """
    con = get_connection()
    df = con.execute(query).df()

    df["service_date"] = pd.to_datetime(df["service_date"], errors="coerce")

    df["claim_age_days"] = (
        pd.Timestamp.today().normalize() - df["service_date"]
    ).dt.days

    df["claim_age_bucket"] = pd.cut(
        df["claim_age_days"],
        bins=[-1, 30, 60, 90, 100000],
        labels=["0-30 days", "31-60 days", "61-90 days", "90+ days"],
    ).astype("object")

    df["claim_age_bucket"] = df["claim_age_bucket"].fillna("unknown")

    df["priority_score"] = (
        df["latest_outstanding"].fillna(0).apply(
            lambda x: 5 if x > 1000 else (3 if x > 250 else 1)
        )
        + df["transaction_count"].fillna(0).apply(
            lambda x: 3 if x >= 10 else (2 if x >= 5 else 0)
        )
        + df["claim_age_days"].fillna(0).apply(
            lambda x: 3 if x > 90 else (2 if x > 60 else 0)
        )
    )

    return df