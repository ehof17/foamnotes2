# Async processing

### Decoupling
- Services don't have to wait for others to finish work to complete their work
- Ecommerce, user places order, inventory update, and email notification can be handled separately

### Scalability
- Workloads can be distributed 


### Reslience
- One service down doesn't break whole system
- Message queue: If one worker goes down, the stuff is still in the queue and can be processed once the worker is back

### Performance
- Doing tasks at same time 
- Uber
- Location updates, driver requests, and updates are all handled at the same time

