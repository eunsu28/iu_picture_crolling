import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.google.com.hk/search?q=%EC%95%84%EC%9D%B4%EC%9C%A0&newwindow=1&safe=strict&sxsrf=ALeKk02Bzz8MyG6co35WF6lyBlv7qU76Zw:1625311624983&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjrmbnQ5cbxAhVOILcAHdPxD-8Q_AUoAXoECAEQAw&biw=1920&bih=969"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
img = soup.find_all("img")
for i in img:
    print(img)


