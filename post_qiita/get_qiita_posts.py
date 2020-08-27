import requests
from secrets import QIITA_ACCESS_TOKEN

headers = {"Authorization": f"Bearer {QIITA_ACCESS_TOKEN}"}
print(headers)
a = requests.get("https://qiita.com/api/v2/authenticated_user/items", headers=headers)

print(a.json())
