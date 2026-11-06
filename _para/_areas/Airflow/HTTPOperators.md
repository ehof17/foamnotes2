# HTTP Operators
- Support Get, post, put, delete

Customizable
- Headers, parameters and body can be specified
  
Response Handling
- Can log responses and process them further in a dag

``` pip install apache-airflow-providers-http```

``` from airflow.providers.http.operations ```


Within airflow ui you can add connection so the dag just has the connectionID, not hard code what the url is or anything

