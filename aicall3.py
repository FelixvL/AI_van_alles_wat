import os
import openai

openai.api_key = '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'

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)