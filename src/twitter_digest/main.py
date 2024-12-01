from dotenv import load_dotenv
import os
from daily_digest import TwitterDigestBot
from models import DigestConfiguration
load_dotenv()  # Load environment variables from .env

twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Create a configuration
config = DigestConfiguration(
    authors=['BitcoinMagazine', 'PunterJeff', 'MSTRUpdates', 'BenWerkman'],  # List of Twitter handles to follow
    categories=['Bitcoin', 'MicroStrategy']  # Categories to sort tweets into
)

bot = TwitterDigestBot(
    twitter_bearer_token=twitter_bearer_token,
    openai_api_key=openai_api_key
)
digest = bot.generate_daily_digest(config) 