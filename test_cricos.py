import requests
from bs4 import BeautifulSoup

url = "https://cricos.education.gov.au/Institution/InstitutionSearch.aspx"
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print("cricos live site status:", res.status_code)
