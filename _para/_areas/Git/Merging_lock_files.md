If you have a big lock file and merge tool doesnt even load, and you just want to take one version of the file, heres what I did
In this scenario I just want to use the lock file from to_90953780_es_migration


git checkout to_90953780_es_migration
git merge master

-- outputted error


git checkout to_90953780_es_migration -- Pipfile.lock
git add Pipfile.lock
git merge --continue
