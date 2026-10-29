from datetime import datetime, timezone

from airflow.sdk import (
    Asset,
    PartitionedAssetTimetable,
    PartitionedAtRuntime,
    dag,
    get_current_context,
    task,
)

from c3_order_support import DATA_DIR, validate_date, accepted_count


partitioned_orders = Asset(
    name="partitioned_validated_orders",
    uri=(DATA_DIR / "partitioned_validated_orders.ready").resolve().as_uri(),
)


@dag(
    dag_id="c3_partitioned_order_producer",
    schedule=PartitionedAtRuntime(),
    start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
    catchup=False,
    is_paused_upon_creation=True,
    tags=["course-3", "partition", "producer"],
)
def partitioned_order_producer():
    @task(outlets=[partitioned_orders])
    def publish_partition(outlet_events) -> None:
        business_date = validate_date(get_current_context()["dag_run"].conf["business_date"])
        assert accepted_count() >= 2, "Sample readiness requires two accepted orders"
        outlet_events[partitioned_orders].add_partitions(business_date)
        print(f"PUBLISHED_PARTITION partition_key={business_date}")

    publish_partition()


@dag(
    dag_id="c3_partitioned_order_report",
    schedule=PartitionedAssetTimetable(assets=partitioned_orders), # scheule carries published key in its run
    start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
    catchup=False,
    is_paused_upon_creation=True,
    tags=["course-3", "partition", "consumer"],
)
def partitioned_order_report():
    @task
    def build_partition_report() -> None:
        dag_run = get_current_context()["dag_run"] # reads its own runs partition key and uses it in the output file name
        output = DATA_DIR / f"order_report_{dag_run.partition_key}.txt"
        output.write_text(f"partition_key={dag_run.partition_key}\n", encoding="utf-8")
        print(f"REPORT_PARTITION partition_key={dag_run.partition_key} output={output}")

    build_partition_report()


partitioned_order_producer()
partitioned_order_report()
