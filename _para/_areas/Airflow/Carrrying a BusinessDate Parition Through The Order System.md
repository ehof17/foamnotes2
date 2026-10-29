# Carry one business date from file arrival, through producer, into report

The report also needs to know which date to process
- Partition key keeps that business date with the work

At landing, we identify which business date the arrival data belongs to
- That date should stay with the work as it moves between workflows.

The producer adds the date to its asset event as the parition key

The update now identifes which part of the data is ready

the partition asset timeline gives the consumer run that key
Its task: Read the key from context to select their work.

When one day needs rebuilding, replay uses the same partiiton key to select that date again
The task must use that key to limit which data it reads and rewrites


#### Prove one parition across five surfaces
**Producer** receives business date in its run input
**Asset update** records that date as the parition key
**Downstream run** Gets the key through its partion asset timeline. A date stored only in ordinary event metadata would not set the run partition automatically
**Task logs** Can record the date used during processing. 


Update the order intake watcher to save receipt
```python
def validate_date(value):
    if not isinstance(value, str) or date.fromisoformat(value).isoformat() != value:
        raise ValueError(f"Invalid date: {value}")
    return value


def save_receipt(claimed, receipt, run_id):
    text = claimed.read_text(encoding="utf-8")
    if not text.startswith("business_date="):
        raise ValueError(f"Invalid claimed file: {claimed}")
    value = validate_date(text.split("=", 1)[1])
    receipt.write_text(json.dumps({"business_date": value, "intake_run_id": run_id}), encoding="utf-8")
    claimed.unlink()

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
        save_receipt(CLAIMED_FLAG, LANDING_FLAG.parent / "arrival-receipt.json", context["dag_run"].run_id) # update
        print("LANDING_STATE reset")

    consume_landing_file()


order_intake_watcher()

```

#### Create c3_partitions

