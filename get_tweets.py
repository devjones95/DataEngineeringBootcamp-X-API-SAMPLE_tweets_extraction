# Importing the necessary libraries
import json
import tweepy
from datetime import datetime

# Registering our Twitter API credentials and Tokens
# Obviously, after the commit on Git, these keys will be changed ;p
consumer_key = 'i7y2X4t3a4bPyMbGnvaIz7nF2'
consumer_secret = 'oFg9LyQFKF2hF1kpS23hsXusGPzT69xrYKhRYBBMyLlExAYOmF'
access_token = '2009575200455786496-j0e2gb60QTejLz7DKvOWlljaQJk9yE'
access_token_secret = '0t7ovh7TgCZzsUT5Fd8nbDDAYNhoIrVt0W7Mryce1p1Xq'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHpy6wEAAAAA32DAjtrUsc7H%2BqXi5spJc4o2eBs%3DHQUSBiycUNsPXmTCB89rl0L7sPgEn9iCBw6VuaY9SIhiTDp4xi'

# Creating an arquive to store the collected tweets with a timestamp and don't overwrite previous data
date_today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
out = open(f"collected_tweets{date_today}.json", "w")

# Creating a class that will listen to the Twitter Stream
class MyStream(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        data = {
            "id": tweet.id,
            "text": tweet.text,
            "created_at": str(tweet.created_at)
        }
        
        with open(output_file, "a", encoding="utf-8") as out:
            out.write(json.dumps(data, ensure_ascii=False) + "\n")

        print(tweet.text)

    def on_errors(self, errors):
        print(errors)
    
    
# Implementing our MAIN function
if __name__ == "__main__":
    stream = MyStream(bearer_token)

    # Remove old rules
    rules = stream.get_rules()
    if rules.data:
        stream.delete_rules([rule.id for rule in rules.data])

    # Adding new rules to filter tweets
    stream.add_rules([
        tweepy.StreamRule("data engineering"),
        tweepy.StreamRule("machine learning"),
        tweepy.StreamRule("AI")
    ])
    
    # Starting the stream
    stream.filter(tweet_fields=["created_at"])
   
        
        
         