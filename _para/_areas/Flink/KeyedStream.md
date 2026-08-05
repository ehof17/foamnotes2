# Keyed stream

- Partioned by particular key
  - Like userID/itemID

All records with same key go to the same keyed subtask
- Guarantees all events for a given ID are processed consistently, even if data is across the cluster
