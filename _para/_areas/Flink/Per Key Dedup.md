
Suppose we want to deduplicate ad clicks, so we only count the first click from a user on a given ad

We would define a [[Keyed State]], keyed by AdID|UserID
- Each subtask stores a bool flag to track if a click has been seen.


```python
from datetime import timedelta
from typing import Iterable

from pyflink.common import Types
from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import StateTtlConfig, ValueStateDescriptor


class FirstSeenDedup(KeyedProcessFunction):
    """
    Emits only the first ClickEvent seen for each keyed adId|userId
    during a 24-hour period.
    """

    def open(self, runtime_context: RuntimeContext) -> None:
        ttl_config = (
            StateTtlConfig.new_builder(timedelta(hours=24))
            .set_update_type(
                StateTtlConfig.UpdateType.OnCreateAndWrite
            )
            .build()
        )

        state_descriptor = ValueStateDescriptor(
            "seen",
            Types.BOOLEAN()
        )
        state_descriptor.enable_time_to_live(ttl_config)

        self.seen = runtime_context.get_state(state_descriptor)

    def process_element(
        self,
        value,
        ctx: KeyedProcessFunction.Context
    ) -> Iterable:
        if self.seen.value() is None:
            self.seen.update(True)
            yield value


```

[Keyed State]: <Keyed State.md> "Keyed State"
