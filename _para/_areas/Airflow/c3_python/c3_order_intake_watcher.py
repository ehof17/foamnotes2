from datetime import datetime, timezone

from airflow.sdk import Asset, AssetWatcher, dag, get_current_context, task

from course3_plugins import FileArrivalTrigger
from c3_order_support import CLAIMED_FLAG, LANDING_FLAG, save_receipt


landing_orders = Asset(
    name="landing_orders",
    uri=LANDING_FLAG.resolve().as_uri(),
    watchers=[
        AssetWatcher(
            name="orders_ready_watcher",
            trigger=FileArrivalTrigger(path=str(LANDING_FLAG), claimed_path=str(CLAIMED_FLAG)),
        )
    ],
)
# Uses asset watcher with file trigger
# That watcher turns the arrival signal into an asset event


@dag(
    dag_id="c3_order_intake_watcher",
    schedule=landing_orders,
    start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
    catchup=False,
    is_paused_upon_creation=True,
    tags=["course-3", "asset-watcher"],
)
def order_intake_watcher():
    @task
    def consume_landing_file() -> None:
        context = get_current_context()
        print(f"WATCHER_EVENT {context['triggering_asset_events']}")
        print(f"CLAIMED_FILE {CLAIMED_FLAG}")
        CLAIMED_FLAG.unlink(missing_ok=True)
        print("LANDING_STATE reset")

    consume_landing_file()


order_intake_watcher()
