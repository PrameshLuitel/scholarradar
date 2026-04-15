import requests
import pandas as pd
import io

url = "https://data.gov.au/data/api/3/action/package_show?id=cricos"
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).json()
latest_url = res['result']['resources'][0]['url']
print("Downloading:", latest_url)

xlsx_data = requests.get(latest_url).content
xl = pd.ExcelFile(io.BytesIO(xlsx_data))
print("Sheet names:", xl.sheet_names)

for sheet in xl.sheet_names:
    print(f"\n--- {sheet} ---")
    df = xl.parse(sheet, nrows=0)
    print(df.columns.tolist())
