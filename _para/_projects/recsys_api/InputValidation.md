### Additional Validation
#### Currently can hit embed api with same id in the samples
```json
{
  "samples": [
    {
      "id": 12345,
      "manufacturer": "John Deere",
      "model": "8320R",
      "condition": "Used",
      "listingstate": "Active",
      "basecategoryid": 1,
      "categoryid": 101,
      "year": 2018,
      "description": "Trandition",
      "evaluation": 185000.0,
      "media_id": 11036280198
    },
       {
      "id": 12345,
      "manufacturer": "John Deere",
      "model": "8320R",
      "condition": "Used",
      "listingstate": "Active",
      "basecategoryid": 1,
      "categoryid": 101,
      "year": 2018,
      "description": "Trandition",
      "evaluation": 185000.0,
      "media_id": 11036280198
    },
       {
      "id": 12345,
      "manufacturer": "John Deere",
      "model": "8320R",
      "condition": "Used",
      "listingstate": "Active",
      "basecategoryid": 1,
      "categoryid": 101,
      "year": 2018,
      "description": "Trandition",
      "evaluation": 185000.0,
      "media_id": 11036280198
    }
  ]
}
```

and it returns an error
```json
{
    "response": [],
    "success": false,
    "message": "[StatusCode.INVALID_ARGUMENT] [request id: <id_unknown>] input 'input_description' batch size does not match other inputs for 'recsys_similar_item'"
}
```

Changing them to have different IDs returns the response, so the error is probably from that.

#### MediaID not required
- Hitting /similar/item/embed without "media_id" in payload returns bad error

```json
{
    "response": [],
    "success": false,
    "message": "list index out of range"
}
```
Or if multiple samples, some with media_id
``` json
{
    "response": [],
    "success": false,
    "message": "nan"
}
```


