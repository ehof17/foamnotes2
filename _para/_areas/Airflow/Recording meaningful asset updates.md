# Publish an update only after readiness check pass
- an update tells the reporting workflow that it can use the data
- We need to check the result before making that announcement

Readiness check should cover what consumer needs
- freshness
- row count
- required columns

If validation fails, the task with the asset outlet must fail too
- Logging an error and returning normally would still count as a task success

We attach metdata that identifies the result, such as business date and how many rows passed
- Airflow records the source DAG and run on the event
Airflow records the asset update when the outlet task succeeds

Our code must check the orderes before reaching that point


Valid result vs one that fails
### success
- Inspect the asset update and the metadata that identifies the result
- Asset update is emitted
- Metadata names the result
### fails
- check that the outlet task fails and no new update appears for that attempt
- Task records evidence
- No update is emitted

### Consumer
- Wait for a successful update
- Use the event to find the checked data
- Reaching the scheduled time alone does not tell it that the data is ready


```python
import json
from datetime import timedelta
from datetime import datetime, timezone

from airflow.sdk import Asset, Metadata, Param, dag, get_current_context, task
from c3_order_support import DATA_DIR, accepted_count, reset_database

# Asset itself does not create a ready file or watch a folder
# task will publish its update when validation succeeds
validated_orders = Asset(
    name="validated_orders",
    uri=(DATA_DIR / "validated_orders.ready").resolve().as_uri()
)
@dag(
    dag_id="produce_validated_orders",
    schedule=None,
    start_date=datetime(2026,1,1, tzinfo=timezone.utc),
    catchup=False,
    is_paused_upon_creation=True,
    params={
        "minimum_accepted_orders":Param(
            1,
            type="integer",
            minimum=1,
            description="Minimum orders required before validate_orders is ready"
        )
    }
)
def produce_validated_orders():
    @task(outlets=[validated_orders])
    def validate_orders():
        batch = json.loads((DATA_DIR / "orders_batch.json").read_text())
        interval_start = datetime.fromisoformat(batch["business_date"]).replace(tzinfo=timezone.utc)
        received_count = reset_database()
        accepted = accepted_count()
        minimum = int(get_current_context()["params"]["minimum_accepted_orders"])
        if accepted < minimum:
            raise ValueError(f"Accepted {accepted} needs {minimum}")

        yield Metadata(
            validated_orders,
            extra={
                "business_date": batch["business_date"],
                "interval_start": interval_start.isoformat(),
                "interval_end": (interval_start + timedelta(days=1)).isoformat(),
                "received_count": received_count,
                "accepted_count": accepted,
                "minimum_accepted_orders": minimum,
                "storage_reference": str(DATA_DIR / "order_processing.db"),
            },
        )
    validate_orders()
produce_validated_orders()
```
