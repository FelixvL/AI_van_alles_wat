import os
import openai
import time
openai.organization = "org-740nV95u1Kb2mEgEERhTe8j9"
openai.api_key = "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"


request.post("https://api.openai.com/v1/chat/completions")
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $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" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}]
  }'

  import requests

def post_message(url, message):
    data = {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print('Message posted successfully.')
    else:
        print('Failed to post message.')

# Example usage
url = 'https://api.openai.com/v1/chat/completions'
message = 'Hello, world!'

post_message(url, message)