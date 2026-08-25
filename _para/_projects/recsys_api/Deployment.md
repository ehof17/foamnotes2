In devops, there is docker-compose-gpu_live
```yaml
services:
  recsys:
    hostname: recsys
    image: mlregistry.sandhills.int/recsys:1.2.2
    logging:
      driver: splunk
      options:
    healthcheck: #<== This makes it so that we can check if the api is successfully running
      test: curl --silent --fail http://0.0.0.0:80/_ping || exit 1
      interval: 30s
      timeout: 5s
      start_period: 600s
    build:
      context: ./
    volumes:
      - "recsys_live:/app/models"
    deploy:
      labels:
        #### Labels define the behavior and rules of the traefik proxy for this container ####
        - "traefik.enable=true" # <== Enable traefik to proxy this container
        - "traefik.stack=sandhills_ml_triton" # This is so multiple traefiks can live on same server
        - "traefik.http.routers.recsys.rule=Headers(`api`,`recsys`)" # <== Your Domain Name goes here for the http rule
        - "traefik.http.routers.recsys.entrypoints=machine_learning_live" # <== Defining the entrypoint for http, **ref: line 30
        - "traefik.http.services.recsys.loadbalancer.server.port=80"
        - "healthcheck_service.enable=true"
        - "healthcheck_service.stack=sandhills_ml_live"
      replicas: 2
      update_config:
        failure_action: rollback
        parallelism: 1
        delay: 30s
      restart_policy:
        condition: any
        delay: 5s
        max_attempts: 3
        window: 240s
    environment:
      - TRITON_URL=TritonMain:8001
    networks:
      - machine_learning_triton
volumes:
  recsys_live:
    external: true
networks:
  machine_learning_triton:
    external: true
```
In Github the recsys service is all defined in single compose

```yaml
  recsys:
    hostname: recsys
    image: mlregistry.sandhills.int/recsys:1.2.1
    healthcheck: #<== This makes it so that we can check if the api is successfully running
      test: curl --silent --fail http://0.0.0.0:80/_ping || exit 1
      interval: 30s
      timeout: 5s
      start_period: 600s
    build:
      context: ./
    environment:
      - ENVIRONMENT=live
    deploy:
      labels:
        #### Labels define the behavior and rules of the traefik proxy for this container ####
        - "traefik.enable=true" # <== Enable traefik to proxy this container
        - "traefik.stack=sandhills_ml_triton" # This is so multiple traefiks can live on same server
        - "traefik.http.routers.recsys.rule=Header(`api`,`recsys`)" # <== Your Domain Name goes here for the http rule
        - "traefik.http.routers.recsys.entrypoints=sandhills_ml_triton" # <== Defining the entrypoint for http, **ref: line 30
        - "traefik.http.services.recsys.loadbalancer.server.port=80"
        - "healthcheck_service.enable=true"
        - "healthcheck_service.stack=sandhills_ml_triton"
      replicas: 10
      update_config:
        failure_action: rollback
        parallelism: 5
        delay: 30s
      restart_policy:
        condition: any
        delay: 5s
        max_attempts: 3
        window: 240s
    networks:
      - machine_learning_bis

```

Is it not working because it is now in the machine_learning_bis network, not machine_learning_triton?


Exec-ing into a running container, looks like the TRITON_URL env variable wasn't set.

The other api is load balanced on http://recsys.sandhills.int:9212
Its traefik.htto.routers. entrypoints is machine_learning_bis
While recsys is sandhills_ml_triton
Maybe I am hitting wrong url?

In the container,  curl localhost:80/_ping returns healthy
