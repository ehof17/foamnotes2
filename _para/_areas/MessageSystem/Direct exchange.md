
# Direct exchange

### Use case
- A user signs up, then some actions must follow.
1. Send an onboarding email, or verify link
2. Log the registration attempt

Data gathered by sign up is published to a RabbitMq Exchange, along the routing keys
In this example, the routing keys are user.create, user.email, and user.logging

User.create -> creates user in database
User.email -> sends the onboarding email
User.logging -> records onboarding event

Each queue has different consumers to create, onboard, and log
If we want to do something like analytics, we can bind a new queue

### Considerations
- Scaling consumer with workload (multiple instances)
- Dead letter queues can help manage failed messages
- Monitoring and logging


