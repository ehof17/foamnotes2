Taskflow task
- suits logic we can write ourselves, like checking an order amount
- values connect like function calls
- Easy pure logic tests


Operators
- Packaged external system action (db command / file transfer)
- Provider owns the integration
- Connections and templates are explicit

Taskflow function: Small python native transformation with  visibile return value

Provider operator: Packaged external system action with its own contract

Separate task: independent retries, ownership, or evidence
