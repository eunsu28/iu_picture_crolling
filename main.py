import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EC%9C%A0"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
a = soup.find_all("img")
print(a)