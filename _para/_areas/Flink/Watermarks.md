
# Watermarks

Define "How late is late"
- Special markers in a stream that tell Flink how far event time has progressed
- Let Flink decide when to close a [[window]] and emit results, even if some events arrive late


Flink supports different watermark strategies
1. Monotonous timestamps
   1. Assume events arrive in perfect order
2. Bounded out of orderness
   1. Allows for some lateness, like up to 5 seconds
Regardless, watermarks flow with the stream, and windows fire when watermark passes the boundary


[window]: windows.md "windows"
