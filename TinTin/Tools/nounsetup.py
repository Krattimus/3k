import requests
import json
import webbrowser
import sys
from tintin import TinTin
url = "https://api.openai.com/v1/images/generations"

payload = json.dumps({
  "prompt": sys.argv[1]
})
headers = {
  'Authorization': 'Bearer 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',
  'Content-Type': 'application/json',
  'Cookie': '__cf_bm=5keMMMocu7nmnRclBj7_NhPZwrf573LVJ8hoQRIU1W4-1704442402-1-ATS5+C1tXrWxA3ZlKhg5WTEc0fDKeylWjIK19O6TgahyaBaD+sgMa4LGhNqZa+KkG6nh8GcXKpmP6aYNC0wm2Ag=; _cfuvid=TZgb9Ydz7s6yky9G5BsylQejpEZ4ll1sBD_CLXQDlUE-1704442402745-0-604800000'
}

response = requests.request("POST", url, headers=headers, data=payload)
json = response.json()

webbrowser.open(json["data"][0]["url"], new=0, autoraise=True)
