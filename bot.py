import tweepy, openai
import os
from dotenv import load_dotenv
import schedule
import time
import logging

# Import the generate_horror_prompt function from our new module
from horror_prompts import generate_horror_prompt

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Set OpenAI key once, outside of the function
openai.api_key = os.getenv("OPENAI_KEY")

# Tweepy Initialization
api = tweepy.Client(os.getenv("BEARER_TOKEN"),
                           os.getenv("API_KEY"),
                           os.getenv("API_KEY_SECRET"),
                           os.getenv("ACCESS_TOKEN"),
                           os.getenv("ACCESS_TOKEN_SECRET"))

def generate_response():
    text = generate_horror_prompt()  # Use the imported function here
    
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=[{"role": "system", "content": "You are a viral twitter content creator"},
                                                          {"role": "user", "content": text}],
                                                max_tokens=100
                                                )
        print(response)
        return response
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return None

def tweet(response):
    if response and 'choices' in response and response['choices']:
        content = response['choices'][0]['message']['content']
        if len(content) <= 280:  # Check tweet length
            try:
                api.create_tweet(text=content)
                logging.info(f"Tweeted: {content}")
            except Exception as e:
                logging.error(f"Error posting tweet: {e}")
        else:
            logging.warning("Generated content exceeds tweet length.")
    else:
        logging.warning("No valid response to tweet.")

def job():
    res = generate_response()
    tweet(res)

# Scheduling
job()
# schedule.every(2).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)