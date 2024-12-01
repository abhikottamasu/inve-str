from typing import List
import tweepy
import time
from models import Tweet

class TweetCollector:
    def __init__(self, bearer_token: str):
        self.client = tweepy.Client(bearer_token=bearer_token)
    
    def _make_api_call_with_retry(self, api_func, *args, max_retries=3, **kwargs):
        for attempt in range(max_retries):
            try:
                return api_func(*args, **kwargs)
            except tweepy.errors.TooManyRequests as e:
                if attempt == max_retries - 1:  # Last attempt
                    raise e
                # Wait with exponential backoff (15 mins * 2^attempt)
                wait_time = 5 * (2 ** attempt)  # in seconds
                print(f"Rate limit exceeded. Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            except Exception as e:
                raise e

    def collect_daily_tweets(self, authors: List[str]) -> List[Tweet]:
        tweets = []
        for author in authors:
            # Get user ID with retry
            user = self._make_api_call_with_retry(
                self.client.get_user,
                username=author
            )
            if not user.data:
                continue
                
            # Get recent tweets with retry
            response = self._make_api_call_with_retry(
                self.client.get_users_tweets,
                user.data.id,
                max_results=100,
                tweet_fields=['created_at', 'text']
            )
            
            if response.data:
                for tweet_data in response.data:
                    tweets.append(Tweet(
                        id=tweet_data.id,
                        author=author,
                        text=tweet_data.text,
                        created_at=tweet_data.created_at
                    ))
        
        return tweets 