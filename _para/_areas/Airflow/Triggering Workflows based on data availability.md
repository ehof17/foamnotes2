# Assets give workflows a shared name for data and a way to report an Updated
Contract
- Shared asset identity
- Workflow producing the data and the workflow using it must agree on the name

Publish an update only after the data checks pass
An early announcement can start the report before its input is ready

The consumer is the workflow that uses the data
- Its schedule can wait for asset updates

Combinations
- We can wait for any source to update or require a base from all the sources we need

# Define data products as Assets
An asset links the workflow that produces that data to the workflow that uses it

Promise: A stable Asset URI names the data result
- We can change the producer code without changing the name
- Consumer still needs a way to find the Data
Event: An update carries readiness and metadata
- metadata can include row count, business dates and storage location
Consumer: downstream dag that uses the asset in its schedule
- An update can then then start it, code reads the triggering events to decide which data to process since several updates may belong to one run.


