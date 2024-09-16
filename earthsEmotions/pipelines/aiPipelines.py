import requests
import os
from dotenv import load_dotenv


class PolarityPipeline:
    def __init__(self) -> None:
        self.base_url = "https://api-inference.huggingface.co/models/avichr/heBERT_sentiment_analysis"
        self.headers = {
            "Authorization": f"Bearer {os.getenv("HUGGINGFACE_TOKEN")}"
        }

    def process_item(self, article, spider):
        body = article['body'][:1024]
        response = requests.post(self.base_url, headers=self.headers, json={
                                 "inputs": body, "options": {"wait_for_model": True}})
        scores = response.json()[0]
        polarity = 0.0
        for score in scores:
            if score['label'] == 'positive':
                polarity = score['score']

        article['polarity'] = polarity

        return article
