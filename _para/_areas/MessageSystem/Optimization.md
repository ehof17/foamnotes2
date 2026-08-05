# Optimization
> Scenario: Consumer cannot acknowledge messages
- The consumer may be able to receive messages, but it can't let the queue know that it did.
- The consumer can fail, but keep consuming messages.
- So we got a ton of stuff just locked up
- If we have 100 messages other workers wont be able to process them
### Prefeching
- To help prevent this
- Prefetch count = 1, means that if this consumer cannot acknowledge one message, it won't process the next one
- If we have a 100 messages, this worker now only tries one, so if it fails other workers can try to complete the request
- 
