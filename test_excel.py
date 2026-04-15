import pandas as pd
import io
import requests

url = "https://data.gov.au/data/dataset/e5ae7059-bfa8-4fa4-a5c0-c13cf3520193/resource/a737a81a-512d-4e97-b982-1c3be34bbe5a/download/cricos-providers-courses-and-locations-as-at-2026-3-2-11-34-49.xlsx"
data = requests.get(url).content
xl = pd.ExcelFile(io.BytesIO(data), engine="openpyxl")
df = xl.parse("Institutions", header=None, nrows=10)
print(df.values.tolist())
