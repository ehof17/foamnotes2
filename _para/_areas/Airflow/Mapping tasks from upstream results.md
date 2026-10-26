# Can map task dynamically from upstream results
- Instead of hardcoding filenames for example, we can make a task instance per file name
- 
```python
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from airflow.sdk import dag, task


@dag(dag_id="c4_mapped_orders")
def mapped_orders():
    @task
    def process_file(file_name):
        folder = Path(os.environ['AIRFLOW_DEMO_ROOT']) / 'data/orders'
        rows = json.loads((folder /file_name).read_text())
        result = {"file":file_name, "amount":sum(r['amount'] for r in rows)}
        print(json.dumps(result))
        return result

    @task
    def discover_files():
        folder = folder = Path(os.environ['AIRFLOW_DEMO_ROOT']) / 'data/orders'
        return sorted(p.name for p in folder.glob("*.json"))
    process_file.expand(file_name=discover_files())

mapped_orders()

```
