# Twitter Streaming Script with Tweepy

## Overview

This script uses the Twitter API v2 and the Tweepy library to collect real-time tweets based on predefined keywords.  
Collected tweets are stored in a timestamped JSON file, ensuring previous data is not overwritten.

## Features

- Real-time tweet collection using Twitter Streaming API
- Keyword-based filtering
- Automatic JSON file generation with timestamp
- UTF-8 encoding support

## Technologies Used

- Python 3
- Tweepy
- Twitter API v2
- JSON
- Datetime

## How It Works

1. Authenticates with the Twitter API using a Bearer Token  
2. Removes any existing stream rules  
3. Adds new filtering rules based on keywords  
4. Listens to the live Twitter stream  
5. Writes each incoming tweet as a JSON object (one per line)  
6. Prints tweet text to the console in real time  

## Collected Data Structure

Each tweet is stored as a JSON object:

```json
{
  "id": "tweet_id",
  "text": "tweet_text",
  "created_at": "tweet_timestamp"
}
```

## Stream Rules

The script filters tweets containing the following keywords:

- data engineering  
- machine learning  
- AI  

## File Output

Output filename pattern:

```
collected_tweetsYYYY-MM-DD_HH-MM-SS.json
```

Each line in the file represents one tweet in JSON format.

## How to Run

1. Install dependencies:
   ```
   pip install tweepy
   ```

2. Replace the API credentials with your own Twitter API keys.

3. Run the script:
   ```
   python script_name.py
   ```

## Important Notes

- Never commit real API keys to a public repository
- This script uses Twitter API v2 Streaming endpoints
- The stream runs indefinitely until manually stopped

## Possible Improvements

- Use environment variables for credentials
- Add reconnection and error handling logic
- Store data in a database or data lake
- Add tweet metrics and metadata

## License

Educational and experimental use only.
