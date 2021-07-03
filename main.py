import requests
from bs4 import BeautifulSoup
import urllib.request 
import random


url = "https://www.google.com.hk/search?q=%EC%95%84%EC%9D%B4%EC%9C%A0&newwindow=1&safe=strict&sxsrf=ALeKk02Bzz8MyG6co35WF6lyBlv7qU76Zw:1625311624983&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjrmbnQ5cbxAhVOILcAHdPxD-8Q_AUoAXoECAEQAw&biw=1920&bih=969"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
img = soup.find_all("img")
n = 0

a = img[1:]
# img = soup.find("img")  # 이미지 태그
# img_src = a.get("src")
# print(img_src)

picture = []
for i in a:
    n += 1
    str(n)
    img_src = i.get("src")
    picture.append(img_src)
    file = urllib.request.urlopen(img_src).read()
    with open(f"{n}iu.jpg",'wb') as f:
        f.write(file)

    # urllib.request.urlretrieve(url + img_src, "/Users/kim-eunsu/Desktop/구글 이미지 크롤링/img")
    