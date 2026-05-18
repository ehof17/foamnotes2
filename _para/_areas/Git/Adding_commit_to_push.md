### Scenario: Pushed a commit to remote and want to add stuff to it
```git add /home/elijah-hoffman@sandhills.int/A/DTA_DataOps/DataOps.wiki/Jenkins-Jobs/machine_learning_bis_recsys/refresh/refresh_logging.md```
```git commit --amend --no-edit```

> Since I already pushed, I have to force
> --force-with-lease overwrites remote branch only if no one else has updated it since my last fetch
``` git push --force-with-lease origin to_95029710/refresh-logging-update ```
