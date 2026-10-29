If a report needs orders and exchange rates it needs to wait for both assets
When a report depends on 2 assets, we need to decide on which update should start it or and.
Let us choose if either update is enough or both are required

Any source ready
- If an update from either source is a reason to refresh the report
- Will need access to both sources even if one changes

All sources ready
- Will wait until all sources are updated
- Both sources are updated, but we still need to check wether the data belongs to the same business date used for a combined report


As 2 updates are separate
If 1 is ready and 2 is missing: consumer waits and no report is run
If both are ready: one run is created, and report starts
Replay on same partion: process same business date the same partition. To keep one report identiy and avoid duplicate, report logic must recognize date and check what was already processed.

```python
import json
from datetime import timedelta
from datetime import datetime, timezone

from airflow.sdk import Asset, Metadata, Param, dag, get_current_context, task
from c3_order_support import DATA_DIR, RATES_PATH

# Asset itself does not create a ready file or watch a folder
# task will publish its update when validation succeeds
validated_orders = Asset(
    name="validated_orders",
    uri=(DATA_DIR / "validated_orders.ready").resolve().as_uri() # Same URI as producer's outlet, so no python imports needed
)
@dag(
    dag_id="daily_order_report",
    schedule=validated_orders & Asset(
        name="exchange_rates", uri=RATES_PATH.resolve().as_uri()
    ), # validated orders as schedule... as soon as the asset updates
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
