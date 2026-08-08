
# Language native functions

Way to develop pulsar functions without having to import a lot of the sdk
If we needed to append an exclamation point, we don't need to learn the whole sdk.
In java we make class Implementing function interface

```java
import java.util.function.Function // No Pulsar module inputted
public class ExclamationFunction implements Function<String, String> {
    @Override
    public String apply(String input) {
        return String.format("%s!", input);
    }
 } 

```

>Sending complex objects
- If we want to process something like ETF, that has a date and price, class that is not primitive
- How can we send it?
- We can do it in native java
```java
import java.util.function.Function;
import demo.etf;

public class ETFAnalyzerFunction implements Function<String, ETF> {
    @Override
    public string apply(String input) {
        ETF etf = ETF.fromInput(input);
        etf.normalizeName();
        return etf;
    }
}
```
We don't know how to Serialize or Deserialize this class
- We can meet in the middle, using the SerDe (Serialize/Deserialize)

```python
class Tweet(object):
    def __init__(self, username, tweet_content):
        self.username = username
        self.tweet_content = tweet_content
```

```python
from pulsar import SerDe

class TweetSerDe(SerDe):

    def serialize(self, input):
        return bytes("{0}|{1}".format(input.username, input.tweet_content))

    def deserialize(self, input_bytes):
        tweet_components = str(input_bytes).split('|')
        return Tweet(tweet_components[0], tweet_componentsp[1])
```

