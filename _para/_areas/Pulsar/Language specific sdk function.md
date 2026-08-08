
# Language specific sdk function

```java
import org.apache.pulsar.functions.api.Context; // Import the context object
import org.apache.pulsar.functions.api.Function; // Import SDK

public class SDKFunction implements Function<String, Void>{
    public Void process(String input, Context context){
        // do something
    }
}
Axel Sirota recommends the Java versh

Context object allows us to get the state of the function
- who am i
- where am i deployed
- do i have cache
-
