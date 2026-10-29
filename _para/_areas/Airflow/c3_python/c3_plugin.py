import asyncio
import os
from pathlib import Path
from typing import Any, AsyncIterator

from airflow.triggers.base import BaseEventTrigger, TriggerEvent


class FileArrivalTrigger(BaseEventTrigger):
    def __init__(self, *, path: str, claimed_path: str, poke_interval: float = 2.0):
        super().__init__()
        self.path = path
        self.claimed_path = claimed_path
        self.poke_interval = poke_interval

    def serialize(self) -> tuple[str, dict[str, Any]]:
        """"
        Lets airflow recreate the trigger with those settings
        """
        return (
            "c3_python.c3_plugin.FileArrivalTrigger",
            {"path": self.path, "claimed_path": self.claimed_path, "poke_interval": self.poke_interval},
        )

    async def run(self) -> AsyncIterator[TriggerEvent]:
        source = Path(self.path)
        claimed = Path(self.claimed_path)
        while True:
            if source.exists(): 
                # when it appears, claim it by moving to the claimed path
                claimed.parent.mkdir(parents=True, exist_ok=True)
                os.replace(source, claimed)
                yield TriggerEvent({"claimed_path": str(claimed), "event": "orders_arrived"})
                return
            await asyncio.sleep(self.poke_interval) # While file absent, file waits
