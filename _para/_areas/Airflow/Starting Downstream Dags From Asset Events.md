Report needs to find orders that caused it to start
- we can follow that connection through the producer, event, and consumer.
- Keep the asset identity and information about the result together so the report can find the data that changed.


### producer
- checks the orders
- publishes an update with business date and storage location

### Asset event
- saves that info, can inspect it to see which results are ready

### Consumer
- when update meets the consumer schedule, airflow can create a run
- Reporting task uses the event information to choose its input

### We will check which update starts the report and which business date reaches its task
- Publish an update that identifies the ready orders and their business date
- The queue records asset updates waiting for the consumer
- Airflow uses queue to check its schedule
- A queue update does not mean a run already exists

In [[Recording meaningful asset updates]] this announces when validated orders are ready
The producers outlet is the validated_orders asset.
The daily report will use that same validated_orders_asset 
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
    uri=(DATA_DIR / "validated_orders.ready").resolve().as_uri() # Same URI as producer's outlet, so no python imports needed
)
@dag(
    dag_id="daily_order_report",
    schedule=validated_orders, # validated orders as schedule... as soon as the asset updates
    start_date=datetime(2026,1,1, tzinfo=timezone.utc),
    catchup=False,
    is_paused_upon_creation=True
)
def daily_order_report():
    @task
    def build_report():
        events = get_current_context()["triggering_asset_events"]
        batch = json.loads((DATA_DIR / "orders_batch.json").read_text())
        matching = [
            event
            for asset, records in events.items()
            if asset.uri == validated_orders.uri
            for event in records
        ]
        assert matching and all(
            e.extra["business_date"] == batch["business_date"] for e in matching
        )
        for event in matching:
            print(f"BATCH_DATE={event.extra['business_date']}")
            print(f"SOURCE_DAG={event.source_dag_id}")
            print(f"SOURCE_RUN={event.source_run_id})
        print("REPORT_READY")
    build_report()
daily_order_report()
```

[Recording meaningful asset updates]: <Recording meaningful asset updates.md> "Publish an update only after readiness check pass"
