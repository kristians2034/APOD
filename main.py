import requests
from datetime import datetime, timedelta
import random

api_key = "5hnCyWjiWuH4eupC07EQ59eQKHNA0PqPeU9XPy5J"

start_date = datetime(1995, 6, 16)
end_date = datetime.now()
random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

date_str = random_date.strftime("%Y-%m-%d")

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date_str}"

response = requests.get(url).json()

image_url = response["url"]
title = response["title"]
explanation = response["explanation"]

print(f"Title: {title}")
print(f"Image URL: {image_url}")
print(f"Explanation: {explanation}")



