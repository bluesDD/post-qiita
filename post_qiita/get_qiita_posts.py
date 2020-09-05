# import requests
import json
from get_secrets import QIITA_TOKEN
import requests

headers = {"Authorization": f"Bearer {QIITA_TOKEN}"}
a = requests.get("https://qiita.com/api/v2/authenticated_user/items", headers=headers)

posts = json.loads(a.text)
for post in posts:
  print(post.keys())

