### using poetry with vscode

poetry init and adding python-dotenv didn't work

```
Add a package (leave blank to skip): python-dotenv
Unable to find package
```
So just had to load the full thing, then add my deps later


```
poetry env info
```
Gave me the virtualenv location

```
Virtualenv
Python:         3.13.12
Implementation: CPython
Path:           /Users/ehof/Library/Caches/pypoetry/virtualenvs/sheetsdatabase-2UPPUbHP-py3.13
Executable:     /Users/ehof/Library/Caches/pypoetry/virtualenvs/sheetsdatabase-2UPPUbHP-py3.13/bin/python
Valid:          True
```

Need to select interpreter in vscode
Then enter the entire python string into it

```
/Users/ehof/Library/Caches/pypoetry/virtualenvs/sheetsdatabase-2UPPUbHP-py3.13/bin/python
```
Voila
