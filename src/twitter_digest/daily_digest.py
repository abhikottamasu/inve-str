from tweet_collector import TweetCollector
from categorizer import TweetCategorizer
from digest_generator import DigestGenerator
from models import DigestConfiguration

class TwitterDigestBot:
    def __init__(self, twitter_bearer_token: str, openai_api_key: str):
        self.tweet_collector = TweetCollector(twitter_bearer_token)
        self.categorizer = TweetCategorizer()
        self.digest_generator = DigestGenerator(openai_api_key)
    
    def generate_daily_digest(self, config: DigestConfiguration) -> str:
        # Collect tweets
        tweets = self.tweet_collector.collect_daily_tweets(config.authors)
        import pdb; pdb.set_trace()
        
        # Categorize tweets
        categorized_tweets = self.categorizer.categorize_tweets(tweets, config.categories)
        
        # Generate digest
        digest = self.digest_generator.generate_digest(categorized_tweets)
        
        return digest 