import requests
import json
url = "https://data.gov.au/data/api/3/action/package_show?id=58ac8ef2-4d2b-4ba5-ae9d-21019058b815"
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(res.status_code)
if res.status_code == 200:
    data = res.json()
    print("Success:", data.get("success"))
    resources = data["result"]["resources"]
    resources.sort(key=lambda x: x.get("created", ""), reverse=True)
    if resources:
        latest = resources[0]
        print("Format:", latest.get("format"))
        print("URL:", latest.get("url"))
        print("Name:", latest.get("name"))
else:
    print(res.text[:200])
