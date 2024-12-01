from typing import List, Dict
from models import Tweet
import openai

class DigestGenerator:
    def __init__(self, openai_api_key: str):
        openai.api_key = openai_api_key
    
    def generate_digest(self, tweets: List[Tweet]) -> str:
        # Group tweets by category
        categorized_tweets: Dict[str, List[Tweet]] = {}
        for tweet in tweets:
            if tweet.category not in categorized_tweets:
                categorized_tweets[tweet.category] = []
            categorized_tweets[tweet.category].append(tweet)
        
        # Generate summary for each category using GPT
        digest = "Daily Twitter Digest\n\n"
        
        for category, category_tweets in categorized_tweets.items():
            digest += f"## {category}\n\n"
            
            # Prepare tweets for summarization
            tweets_text = "\n".join([t.content for t in category_tweets])
            
            # Generate summary using GPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes tweets."},
                    {"role": "user", "content": f"Summarize these tweets in a concise paragraph:\n{tweets_text}"}
                ]
            )
            
            digest += f"{response.choices[0].message.content}\n\n"
        
        return digest 