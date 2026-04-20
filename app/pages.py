import html
import pandas as pd
import plotly.express as px
import streamlit as st

from ui_helpers import format_currency, priority_badge, render_kpi, section_spacer


PLOT_CONFIG = {"displayModeBar": False, "responsive": True}


def style_fig(fig, height=360, *, bars: bool = False):
    layout_kwargs = dict(
        template="plotly_white",
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(252, 254, 253, 0.94)",
        font=dict(family="DM Sans, sans-serif", color="#20384a", size=13),
        margin=dict(l=10, r=10, t=10, b=10),
        height=height,
        legend_title_text="",
        hoverlabel=dict(
            bgcolor="#ffffff",
            font_size=13,
            font_family="DM Sans, sans-serif",
            bordercolor="#c8dbd6",
        ),
    )
    if bars:
        layout_kwargs["bargap"] = 0.28
    fig.update_layout(**layout_kwargs)
    fig.update_xaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        linecolor="#b8d4ce",
        tickfont=dict(color="#4d6570", size=12),
        ticklen=4,
    )
    fig.update_yaxes(
        title=None,
        gridcolor="rgba(24, 75, 84, 0.06)",
        zeroline=False,
        linecolor="#b8d4ce",
        tickfont=dict(color="#4d6570", size=12),
        ticklen=4,
    )
    return fig


def polish_bars(fig):
    fig.update_traces(marker_line=dict(width=0), selector=dict(type="bar"))


def render_page_hero(title, subtitle):
    st.markdown(
        f"""
        <div class="page-hero">
            <div class="page-hero__accent"></div>
            <div class="page-title">{title}</div>
            <div class="page-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_panel_title(title):
    st.markdown(f'<div class="section-heading">{title}</div>', unsafe_allow_html=True)


def render_command_center(filtered_df):
    render_page_hero(
        "Claims command center",
        "Monitor volume, outstanding balances, aging, and priority mix across your portfolio in one operational view.",
    )

    total_claims = len(filtered_df)
    total_outstanding = filtered_df["latest_outstanding"].sum()
    high_priority_count = (filtered_df["financial_priority_bucket"] == "high").sum()
    avg_outstanding = filtered_df["latest_outstanding"].mean() if total_claims else 0
    avg_txn = filtered_df["transaction_count"].mean() if total_claims else 0
    aged_90 = (filtered_df["claim_age_bucket"] == "90+ days").sum()

    r1c1, r1c2, r1c3 = st.columns(3, gap="large")
    render_kpi(r1c1, "Total Claims", f"{total_claims:,}", emphasis=True)
    render_kpi(r1c2, "Total Outstanding", format_currency(total_outstanding), emphasis=True)
    render_kpi(r1c3, "High Priority Claims", f"{high_priority_count:,}", emphasis=True)

    r2c1, r2c2, r2c3 = st.columns(3, gap="large")
    render_kpi(r2c1, "Avg Outstanding", format_currency(avg_outstanding))
    render_kpi(r2c2, "Avg Transactions", f"{avg_txn:.1f}")
    render_kpi(r2c3, "Claims Aged 90+", f"{aged_90:,}")

    section_spacer("lg")

    left, right = st.columns([1.45, 1], gap="large")

    with left:
        with st.container(border=True):
            render_panel_title("Claims by Service Month")
            monthly = filtered_df.copy()
            monthly["service_month"] = monthly["service_date"].dt.to_period("M").astype(str)
            monthly_chart = (
                monthly.groupby("service_month", dropna=False)
                .size()
                .reset_index(name="claim_count")
            )
            fig1 = px.line(
                monthly_chart,
                x="service_month",
                y="claim_count",
                markers=True,
                color_discrete_sequence=["#2a8f82"],
            )
            style_fig(fig1, height=360)
            fig1.update_traces(
                line=dict(width=2.5),
                marker=dict(size=9, line=dict(width=1, color="#ffffff")),
            )
            st.plotly_chart(fig1, use_container_width=True, config=PLOT_CONFIG)

    with right:
        with st.container(border=True):
            render_panel_title("Claims by Priority Bucket")
            priority_chart = (
                filtered_df.groupby("financial_priority_bucket", dropna=False)
                .size()
                .reset_index(name="claim_count")
            )
            priority_chart["financial_priority_bucket"] = pd.Categorical(
                priority_chart["financial_priority_bucket"],
                categories=["high", "medium", "low"],
                ordered=True,
            )
            priority_chart = priority_chart.sort_values("financial_priority_bucket")

            fig2 = px.bar(
                priority_chart,
                x="financial_priority_bucket",
                y="claim_count",
                color="financial_priority_bucket",
                color_discrete_map={
                    "high": "#eb6a6a",
                    "medium": "#f1b458",
                    "low": "#69b8af",
                },
            )
            style_fig(fig2, height=360, bars=True)
            polish_bars(fig2)
            fig2.update_layout(showlegend=False)
            st.plotly_chart(fig2, use_container_width=True, config=PLOT_CONFIG)

    left2, right2 = st.columns(2, gap="large")

    with left2:
        with st.container(border=True):
            render_panel_title("Top Organizations by Outstanding")
            org_chart = (
                filtered_df.groupby("organization_name", dropna=False)["latest_outstanding"]
                .sum()
                .reset_index()
                .sort_values("latest_outstanding", ascending=False)
                .head(10)
            )
            fig3 = px.bar(
                org_chart,
                x="latest_outstanding",
                y="organization_name",
                orientation="h",
                color_discrete_sequence=["#8ccdc5"],
            )
            style_fig(fig3, height=400, bars=True)
            polish_bars(fig3)
            fig3.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig3, use_container_width=True, config=PLOT_CONFIG)

    with right2:
        with st.container(border=True):
            render_panel_title("Claims by Age Bucket")
            age_chart = (
                filtered_df.groupby("claim_age_bucket", dropna=False)
                .size()
                .reset_index(name="claim_count")
            )
            age_chart["claim_age_bucket"] = pd.Categorical(
                age_chart["claim_age_bucket"],
                categories=["0-30 days", "31-60 days", "61-90 days", "90+ days", "unknown"],
                ordered=True,
            )
            age_chart = age_chart.sort_values("claim_age_bucket")

            fig4 = px.bar(
                age_chart,
                x="claim_age_bucket",
                y="claim_count",
                color="claim_age_bucket",
                color_discrete_map={
                    "0-30 days": "#67c8bb",
                    "31-60 days": "#9cd8d1",
                    "61-90 days": "#f5c37a",
                    "90+ days": "#e4aaaa",
                    "unknown": "#d6dde3",
                },
            )
            style_fig(fig4, height=400, bars=True)
            polish_bars(fig4)
            fig4.update_layout(showlegend=False)
            st.plotly_chart(fig4, use_container_width=True, config=PLOT_CONFIG)

    section_spacer("md")

    with st.container(border=True):
        render_panel_title("Top Claims Requiring Attention")
        top_claims = filtered_df.sort_values(
            ["priority_score", "latest_outstanding"],
            ascending=[False, False],
        )[
            [
                "claim_id",
                "provider_name",
                "organization_name",
                "service_date",
                "latest_outstanding",
                "claim_age_bucket",
                "financial_priority_bucket",
                "priority_score",
            ]
        ].head(10).copy()

        top_claims["service_date"] = top_claims["service_date"].dt.strftime("%Y-%m-%d")
        top_claims["latest_outstanding"] = top_claims["latest_outstanding"].map(format_currency)

        st.dataframe(top_claims, use_container_width=True, hide_index=True)


def render_priority_queue(filtered_df):
    render_page_hero(
        "Priority queue",
        "Ranked view of claims that deserve attention first—filtered live from the same rules as your command center.",
    )

    total_filtered = len(filtered_df)
    high_priority = (filtered_df["financial_priority_bucket"] == "high").sum()
    filtered_outstanding = filtered_df["latest_outstanding"].sum()
    avg_age = filtered_df["claim_age_days"].dropna().mean() if total_filtered else 0
    avg_priority_score = filtered_df["priority_score"].mean() if total_filtered else 0

    c1, c2, c3 = st.columns(3, gap="large")
    render_kpi(c1, "Filtered Claims", f"{total_filtered:,}", emphasis=True)
    render_kpi(c2, "High Priority", f"{high_priority:,}", emphasis=True)
    render_kpi(c3, "Filtered Outstanding", format_currency(filtered_outstanding), emphasis=True)

    c4, c5 = st.columns(2, gap="large")
    render_kpi(c4, "Avg Claim Age", f"{avg_age:.0f} days")
    render_kpi(c5, "Avg Priority Score", f"{avg_priority_score:.1f}")

    section_spacer("lg")

    left, right = st.columns([1.15, 1], gap="large")

    with left:
        with st.container(border=True):
            render_panel_title("Priority Mix")
            queue_priority = (
                filtered_df.groupby("financial_priority_bucket", dropna=False)
                .size()
                .reset_index(name="claim_count")
            )
            queue_priority["financial_priority_bucket"] = pd.Categorical(
                queue_priority["financial_priority_bucket"],
                categories=["high", "medium", "low"],
                ordered=True,
            )
            queue_priority = queue_priority.sort_values("financial_priority_bucket")

            fig1 = px.bar(
                queue_priority,
                x="financial_priority_bucket",
                y="claim_count",
                color="financial_priority_bucket",
                color_discrete_map={
                    "high": "#eb6a6a",
                    "medium": "#f1b458",
                    "low": "#69b8af",
                },
            )
            style_fig(fig1, height=320, bars=True)
            polish_bars(fig1)
            fig1.update_layout(showlegend=False)
            st.plotly_chart(fig1, use_container_width=True, config=PLOT_CONFIG)

    with right:
        with st.container(border=True):
            render_panel_title("Aging Distribution")
            queue_age = (
                filtered_df.groupby("claim_age_bucket", dropna=False)
                .size()
                .reset_index(name="claim_count")
            )
            queue_age["claim_age_bucket"] = pd.Categorical(
                queue_age["claim_age_bucket"],
                categories=["0-30 days", "31-60 days", "61-90 days", "90+ days", "unknown"],
                ordered=True,
            )
            queue_age = queue_age.sort_values("claim_age_bucket")

            fig2 = px.bar(
                queue_age,
                x="claim_age_bucket",
                y="claim_count",
                color="claim_age_bucket",
                color_discrete_map={
                    "0-30 days": "#67c8bb",
                    "31-60 days": "#9cd8d1",
                    "61-90 days": "#f5c37a",
                    "90+ days": "#e4aaaa",
                    "unknown": "#d6dde3",
                },
            )
            style_fig(fig2, height=320, bars=True)
            polish_bars(fig2)
            fig2.update_layout(showlegend=False)
            st.plotly_chart(fig2, use_container_width=True, config=PLOT_CONFIG)

    section_spacer("md")

    with st.container(border=True):
        render_panel_title("Priority Queue Table")
        queue_df = filtered_df.sort_values(
            ["priority_score", "latest_outstanding"],
            ascending=[False, False],
        )[
            [
                "claim_id",
                "provider_name",
                "organization_name",
                "service_date",
                "status_primary",
                "latest_outstanding",
                "claim_outstanding_total",
                "transaction_count",
                "claim_age_bucket",
                "financial_priority_bucket",
                "priority_score",
            ]
        ].copy()

        queue_df["service_date"] = queue_df["service_date"].dt.strftime("%Y-%m-%d")
        queue_df["latest_outstanding"] = queue_df["latest_outstanding"].map(format_currency)
        queue_df["claim_outstanding_total"] = queue_df["claim_outstanding_total"].map(format_currency)

        st.dataframe(queue_df, use_container_width=True, hide_index=True)

    with st.container(border=True):
        render_panel_title("Open Claim Detail")
        if not filtered_df.empty:
            selected_claim = st.selectbox(
                "Select Claim ID",
                filtered_df["claim_id"].astype(str).tolist(),
            )
            if st.button("Open selected claim in workspace"):
                st.session_state.selected_claim_id = selected_claim
                st.success(f"Claim {selected_claim} is now selected.")
                st.markdown(
                    '<p class="hint-text">Switch to <strong>Claim detail</strong> in the sidebar to open the full workspace.</p>',
                    unsafe_allow_html=True,
                )
        else:
            st.info("No claims match the current filter set.")


def render_claim_detail(filtered_df):
    render_page_hero(
        "Claim detail workspace",
        "Inspect a single claim end-to-end: balances, clinical and payer context, and the rationale behind its priority score.",
    )

    claim_ids = filtered_df["claim_id"].astype(str).tolist()

    if not claim_ids:
        st.info("No claims match the current filter set.")
        return

    default_index = 0
    if st.session_state.selected_claim_id in claim_ids:
        default_index = claim_ids.index(st.session_state.selected_claim_id)

    selected_claim_id = st.selectbox("Claim ID", claim_ids, index=default_index)
    st.session_state.selected_claim_id = selected_claim_id

    claim_row = filtered_df[filtered_df["claim_id"].astype(str) == str(selected_claim_id)].iloc[0]

    c1, c2, c3 = st.columns(3, gap="large")
    render_kpi(c1, "Claim ID", str(claim_row["claim_id"]), emphasis=True)
    render_kpi(c2, "Priority Score", f"{claim_row['priority_score']:.0f}", emphasis=True)
    render_kpi(c3, "Latest Outstanding", format_currency(claim_row["latest_outstanding"]), emphasis=True)

    c4, c5 = st.columns(2, gap="large")
    render_kpi(
        c4,
        "Claim Age",
        f"{claim_row['claim_age_days']:.0f} days" if pd.notnull(claim_row["claim_age_days"]) else "N/A",
    )
    render_kpi(c5, "Transactions", f"{claim_row['transaction_count']:.0f}")

    section_spacer("lg")

    tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Financials", "Context", "Why Flagged"])

    with tab1:
        with st.container(border=True):
            summary_df = pd.DataFrame(
                {
                    "Field": [
                        "Claim ID",
                        "Service Date",
                        "Primary Status",
                        "Secondary Status",
                        "Patient Status",
                        "Priority Bucket",
                        "Age Bucket",
                    ],
                    "Value": [
                        claim_row["claim_id"],
                        claim_row["service_date"].strftime("%Y-%m-%d") if pd.notnull(claim_row["service_date"]) else "N/A",
                        claim_row["status_primary"],
                        claim_row["status_secondary"],
                        claim_row["status_patient"],
                        claim_row["financial_priority_bucket"],
                        claim_row["claim_age_bucket"],
                    ],
                }
            )
            st.dataframe(summary_df, use_container_width=True, hide_index=True)

    with tab2:
        with st.container(border=True):
            financials_df = pd.DataFrame(
                {
                    "Metric": [
                        "Latest Outstanding",
                        "Claim Outstanding Total",
                        "Total Transaction Amount",
                        "Total Payments",
                        "Total Adjustments",
                        "Total Transfers",
                        "Transaction Count",
                    ],
                    "Value": [
                        format_currency(claim_row["latest_outstanding"]),
                        format_currency(claim_row["claim_outstanding_total"]),
                        format_currency(claim_row["total_transaction_amount"]),
                        format_currency(claim_row["total_payments"]),
                        format_currency(claim_row["total_adjustments"]),
                        format_currency(claim_row["total_transfers"]),
                        f"{claim_row['transaction_count']:.0f}",
                    ],
                }
            )
            st.dataframe(financials_df, use_container_width=True, hide_index=True)

    with tab3:
        with st.container(border=True):
            context_df = pd.DataFrame(
                {
                    "Field": [
                        "Provider",
                        "Specialty",
                        "Organization",
                        "Patient City",
                        "Patient State",
                    ],
                    "Value": [
                        claim_row["provider_name"],
                        claim_row["specialty"],
                        claim_row["organization_name"],
                        claim_row["patient_city"],
                        claim_row["patient_state"],
                    ],
                }
            )
            st.dataframe(context_df, use_container_width=True, hide_index=True)

    with tab4:
        with st.container(border=True):
            reasons = []

            if claim_row["latest_outstanding"] > 1000:
                reasons.append("High latest outstanding amount")
            elif claim_row["latest_outstanding"] > 250:
                reasons.append("Moderate outstanding amount")

            if pd.notnull(claim_row["claim_age_days"]) and claim_row["claim_age_days"] > 90:
                reasons.append("Claim is aged beyond 90 days")
            elif pd.notnull(claim_row["claim_age_days"]) and claim_row["claim_age_days"] > 60:
                reasons.append("Claim is aged beyond 60 days")

            if claim_row["transaction_count"] >= 10:
                reasons.append("High transaction complexity")
            elif claim_row["transaction_count"] >= 5:
                reasons.append("Moderate transaction complexity")

            if not reasons:
                reasons.append("Lower relative operational / financial risk based on current rules")

            items = "".join(f"<li>{html.escape(r)}</li>" for r in reasons)
            st.markdown(
                f"""
                <div class="insight-block">
                    <h3>Why this claim is flagged</h3>
                    <ul class="insight-list">{items}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="insight-block" style="margin-top: 1rem;">
                    <h3>Financial priority bucket</h3>
                    {priority_badge(claim_row["financial_priority_bucket"])}
                </div>
                """,
                unsafe_allow_html=True,
            )