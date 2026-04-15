import requests

url = "https://data.gov.au/data/api/3/action/package_show?id=cricos"
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(res.status_code)
if res.status_code == 200:
    data = res.json()
    resources = data['result']['resources']
    for r in resources:
        print(r['format'], r['url'])
else:
    print(res.text[:200])
