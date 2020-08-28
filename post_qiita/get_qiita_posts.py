import requests
from secrets import QIITA_ACCESS_TOKEN
import json

headers = {"Authorization": f"Bearer {QIITA_ACCESS_TOKEN}"}
print(headers)
a = requests.get("https://qiita.com/api/v2/authenticated_user/items", headers=headers)

posts = json.loads(a.text)
for post in posts:
  print(post.keys())

