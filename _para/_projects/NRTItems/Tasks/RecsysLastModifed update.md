
# RecsysLastModifed update

- Add RecsysLastModifedUTCDateTime to ES index
- Create script that scans active listing files and items in ES index with a RecsysLast within 24 hours

- Output a summary report with the listing Ids and the respective operation:
- If the item is in ES and not in file: delete
- If item is in file and not in ES: add 
- If item is in both: potential update
