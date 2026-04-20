select
    claim_id,

    count(*) as transaction_count,

    sum(coalesce(amount, 0)) as total_transaction_amount,
    sum(coalesce(payments, 0)) as total_payments,
    sum(coalesce(adjustments, 0)) as total_adjustments,
    sum(coalesce(transfers, 0)) as total_transfers,

    max(coalesce(outstanding, 0)) as latest_outstanding,

    min(from_date) as first_transaction_date,
    max(to_date) as last_transaction_date,

    count(distinct transaction_type) as transaction_type_count,
    count(distinct procedure_code) as procedure_code_count

from {{ ref('stg_claims_transactions') }}
group by 1