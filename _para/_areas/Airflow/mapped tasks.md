
# mapped tasks

- 2 files can create 2 mapped task instances
north.json and east.json are 2 files

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
        # pseudo
        rows = json.loads(file_name)
        result = {"file":file_name, "amount":sum(r['amount'] for r in rows)}
        print(result)
        return result
    process_file.expand(file_name=['north.json', 'east.json'])
mapped_orders()

```
Write the processing code once, and airflow can run it for multiple files
