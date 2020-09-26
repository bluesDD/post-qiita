# import requests
import json
from get_secrets import QIITA_TOKEN
import urllib.request
from model import User, Post

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
        try:
            with urllib.request.urlopen(req) as res:
                body = json.load(res)
                return body
        except urllib.HTTPError as err:
            raise err


class QiitaGetInfo:
    """
    Get info from body
    """

    def __init__(self, body):
        self.body = body
    
    def get_updated_date(self):
        updated_at_list = [item["updated_at"] for item in self.body]
        return updated_at_list

    def get_tags(self):
        return [item["tag"] for item in self.body]

    def get_body(self):
        return [item["body"] for item in self.body]

    def get_title(self):
        return [item["title"] for item in self.body]

    def get_created_at(self):
        return [item["created_at"] for item in self.body]

    def get_likes_count(self):
        return [item["likes_count"] for item in self.body]

    def get_url(self):
        return [item["url"] for item in self.body]


if __name__ == "__main__":
    headers = {"Authorization": f"Bearer {QIITA_TOKEN}"}
    qc = QiitaApiClient(base_url, headers)
    body = qc.get_requests("authenticated_user/items")
    body_info = QiitaGetInfo(body)
    print(body_info.get_updated_date())

# a = requests.get("https://qiita.com/api/v2/authenticated_user/items", headers=headers)

# posts = json.loads(a.text)
# for post in posts:
  # print(post["updated_at"], post["title"])

