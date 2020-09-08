# import requests
import json
from get_secrets import QIITA_TOKEN
import urllib.request

base_url = "https://qiita.com/api/v2/"

class QiitaApiClient:
    """
    HttpClient
    """

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get_requests(self, path, params=None):
        url = self.base_url + path
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
          body = res.read()
          return print(body)

if __name__ == "__main__":
    headers = {"Authorization": f"Bearer {QIITA_TOKEN}"}
    qc = QiitaApiClient(base_url, headers)
    qc.get_requests("authenticated_user/items")

# a = requests.get("https://qiita.com/api/v2/authenticated_user/items", headers=headers)
# 
# posts = json.loads(a.text)
# for post in posts:
  # print(post["updated_at"], post["title"])

