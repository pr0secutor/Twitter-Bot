import tweepy, openai, random
import os
from dotenv import load_dotenv

import schedule
import time


load_dotenv()

def generate_response():

    openai.api_key=os.getenv("OPENAI_KEY")

    prompts = [
    {
        "text": "Write a line love story"
    },
    {
        "text": "Write a line horror story"
    },
    {
        "text": "Write a short line murder mystery"
    }
    ]

    text = random.choice(prompts)["text"]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": "You are a genious author"},
                                            {"role": "user", "content": text}],
                                            max_tokens=60
                                            )
    print(response)
    return response

def tweet(response):
    client = tweepy.Client(os.getenv("BEARER_TOKEN"),
                           os.getenv("API_KEY"),
                           os.getenv("API_KEY_SECRET"),
                           os.getenv("ACCESS_TOKEN"),
                           os.getenv("ACCESS_TOKEN_SECRET"))
    
    auth=tweepy.OAuth1UserHandler(os.getenv("API_KEY"),
                                  os.getenv("API_KEY_SECRET"),
                                  os.getenv("ACCESS_TOKEN"),
                                  os.getenv("ACCESS_TOKEN_SECRET"))
    
    api=tweepy.API(auth)
    client.create_tweet(text=response['choices'][0]['message']['content'])

def job():
    res=generate_response()
    tweet(res)

schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


