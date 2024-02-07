import requests
import json
import webbrowser
import sys

url = "https://api.openai.com/v1/images/generations"

payload = json.dumps({
  "prompt": sys.argv[1],
  "model": "dall-e-3",
  "size": "1024x1024",
  "quality": "hd",
  "n": 1
})

headers = {
  'Authorization': 'Bearer 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',
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)
json = response.json()
webbrowser.open(json["data"][0]["url"], new=0, autoraise=True)


