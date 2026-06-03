### Want to make a proxy to redis/es/qdrant that delegates what server to write to or read from


- Reading should be load balanced
- Writing we will need to determine what server to write to
- For ES, we have to hit an API to determine the hot campus

https://refactoring.guru/design-patterns/proxy
Interested in this proxy design

> If theres no pre-existing service interface, create one to make proxy and service objects interchangeable. Extracting the interface from the service class isn’t always possible, because you’d need to change all of the service’s clients to use that interface. Plan B is to make the proxy a subclass of the service class, and this way it’ll inherit the interface of the service.

- Python projects dont have interfaces but are duck types
- Could introduce a subclass
- 
> Create the proxy class. It should have a field for storing a reference to the service. Usually, proxies create and manage the whole life cycle of their services. On rare occasions, a service is passed to the proxy via a constructor by the client.

> Implement the proxy methods according to their purposes. In most cases, after doing some work, the proxy should delegate the work to the service object.

> Consider introducing a creation method that decides whether the client gets a proxy or a real service. This can be a simple static method in the proxy class or a full-blown factory method.

With Adapter you access an existing object via different interface. 


rn, if elastic/qdrant/redis makes an update 
