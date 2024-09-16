import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/avichr/heBERT_sentiment_analysis"
headers = {"Authorization": f"Bearer {os.getenv("HUGGINGFACE_TOKEN")}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json={
                             "inputs": payload, "options": {"wait_for_model": True}})
    return response.json()


data = query(
    "Makerere University’s Brian Ainamaani is among the few Ugandans that have identified and are able to use their talent to earn a living. The third year student of film is a talented artist whose wowing pieces have been admired and appreciated by great figures in this country. Some of Ainamaani’s art pieces live rent free in state House with his latest piece which he donated to Buganda’s Nnaabagereka hanging somewhere in Bulange.  I am a third year student of film and GRC school of liberal and performing arts. I am a skilled and talented artist with a passion for creating unique art pieces. Am a student leader, and well known for my leadership skills, and power with an ability to motivate others. Meeting with the president of this country H. E Yoweri Kaguta Museveni. My greatest accomplishment was creating  mak@100 portraits that honoured the presence of the president.  These pieces are commissioned by the university.  It was an honor to create something that was to be gifted to the president of the country on such a profound day (mak@100 main celebration), it remains one of my proudest achievements.  Presenting my work to such an esteemed figure was a once-in-a-lifetime opportunity. It was a true honor to showcase my art in front of someone who holds such a high position in the cultural heritage of Buganda. It’s a moment I can never take lightly. To have my art recognized by the Nnabagereka was a validation of my artistic abilities and a humbling experience that I’m incredibly grateful for Makerere’s support to developing Talent and i thank my Good Papa Mr. Awel Uwihanganye for the continued support, and also the VC prof. Barnabas Nawangwe for the love ever since he noticed my talent. its been extremely blessing. Indeed he is a parent to cherish. Hmmm, well, being an artist isn’t always a cakewalk, you know. coz there have been plenty of trying moments, but one that really stands out was when I was commissioned to create a large-scale canvas painting, and things kept going wrong.  From delays in material delivery to unexpected technical issues, it felt like everything was working against me. I had to push through countless setbacks, work through sleepless nights, and stay laser-focused to deliver on time. But in the end, I pulled it off, and the final piece was met though stayed in my gallery. Well, that really depends on the piece and the client, but I try to be fair and transparent about my pricing. It’s a delicate balance between honoring the time and effort that goes into my work and making it accessible to a wide range of clients.  I factor in the materials, labor, and any additional costs, as well as my experience and reputation in the field. Ultimately, I want my pricing to reflect the value that my art brings to clients and the joy and inspiration it provides to viewers.  A piece starts at 300,000 ugx shs. as the smallest piece, and takes ahead to 3million according to size.  Man, it’s been a wild ride. I’ve been doodling and drawing since I was a kid, but I started taking my art more seriously in high school. I remember staying up late, sketching and experimenting with different mediums, and finding my own style and voice.  After finishing high school, I decided to pursue art full-time as my daily take , and I’ve been hustling ever since. It’s been a rollercoaster of rejections, successes, and lessons learned, but every step of the way has been worth it.  I’m grateful to be living my dream and sharing my art with the world. Future plans?…I envision a swanky, high-end auction house showcasing my works alongside other established artists and a varied range of pieces, doing local and international sales where pieces can be bought from. Brian Ainamaani  Tel: 0776026565"[:1024])
print(data)
