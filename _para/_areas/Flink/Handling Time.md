Event Time vs Processing timedelta


### Event Time
- Something actually happens

### Processing Time
- When flink actually gets the event.

Flink uses [[windows]] to process [[Unbounded streams]]

What happens when data arrives late?
Flink lets you configure lateness tolerance
- How long to wait for late events
- Can direct very late events to a side output for separate processing

Out of order events are common. Clicks from different regions might take longer to arrive. To tell how late is late, Flink uses [[Watermarks]]

[Unbounded streams]: <Unbounded streams.md> "Unbounded streams"
[windows]: windows.md "windows"
[Watermarks]: Watermarks.md "Watermarks"
