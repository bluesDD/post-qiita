# import requests
import json
from get_secrets import QIITA_TOKEN
import urllib.request

base_url = "https://qiita.com/api/v2/"

class QiitaApiClient:
    """
    HttpClient
    """

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def get_requests(self, path):
        url = self.base_url + path
        req = urllib.request.Request(url)
        if self.headers:
            req.headers = self.headers
        with urllib.request.urlopen(req) as res:
          body = json.load(res)
          return body
    

if __name__ == "__main__":
    headers = {"Authorization": f"Bearer {QIITA_TOKEN}"}
    qc = QiitaApiClient(base_url, headers)
    body = qc.get_requests("authenticated_user/items")
    for i in body:
        print(i["updated_at"])

# 
# a = requests.get("https://qiita.com/api/v2/authenticated_user/items", headers=headers)
# 
# posts = json.loads(a.text)
# for post in posts:
  # print(post["updated_at"], post["title"])

