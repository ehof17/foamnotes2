### Getting stats from a running container

```
docker stats $(docker ps --filter name=recsys --format "{{.ID}}")
```

Will output something like 
CONTAINER ID   NAME                                                            CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O        PIDS 
6b83c7e0f3fa   recsys_iterable_evaluation-recsys-stream-agg-run-31b1e40314ed   --        -- / --               --        --                --               -- 
8f7bd21ae3ac   sandhills_ml_bis_staging_recsys.1.4preu5wpl15rd474hzi3vr2uv     0.00%     982.7MiB / 754.5GiB   0.13%     2.42MB / 47.4kB   34.5MB / 13MB    131 
a884f0b5b243   sandhills_ml_bis_staging_recsys.2.xss8wkvq61d4caqtlsr1raw4k     0.00%     982MiB / 754.5GiB     0.13%     2.42MB / 38.2kB   1.5GB / 71.5MB   131 
