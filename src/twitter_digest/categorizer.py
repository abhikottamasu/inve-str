from typing import List
import spacy
from models import Tweet

class TweetCategorizer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    
    def categorize_tweets(self, tweets: List[Tweet], categories: List[str]) -> List[Tweet]:
        # This is a simple implementation - you might want to use more sophisticated
        # classification methods like machine learning models
        for tweet in tweets:
            doc = self.nlp(tweet.content.lower())
            
            # Simple keyword matching for categories
            for category in categories:
                if category.lower() in doc.text:
                    tweet.category = category
                    break
            
            # Default category if none matched
            if not tweet.category:
                tweet.category = "Miscellaneous"
        
        return tweets 