import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
name = input('Enter picture type?\n')
response = openai.Image.create(
  prompt=name,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)