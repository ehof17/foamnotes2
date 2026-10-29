from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from datetime import date

DEMO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = DEMO_ROOT / "data"
DATABASE_PATH = DATA_DIR / "order_processing.db"
ORDERS_PATH = DATA_DIR / "orders.json"
RATES_PATH = DATA_DIR / "exchange_rates.json"
LANDING_DIR = DATA_DIR / "landing"
LANDING_FLAG = LANDING_DIR / "orders.ready" # signals an arrival
CLAIMED_FLAG = LANDING_DIR / "orders.claimed" # Trigger will rename it to orders.claimed when it picks up a signal





def reset_database() -> int:
    orders = json.loads(ORDERS_PATH.read_text(encoding="utf-8"))
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("DROP TABLE IF EXISTS orders")
        connection.execute(
            "CREATE TABLE orders(order_id INTEGER PRIMARY KEY, customer TEXT, amount REAL, status TEXT)"
        )
        connection.executemany(
            "INSERT INTO orders(order_id, customer, amount, status) VALUES (:order_id, :customer, :amount, :status)",
            orders,
        )
        connection.commit()
def reset_landing_files() -> None:
    LANDING_DIR.mkdir(parents=True, exist_ok=True)
    LANDING_FLAG.unlink(missing_ok=True)
    CLAIMED_FLAG.unlink(missing_ok=True)

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
