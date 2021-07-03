import requests
from bs4 import BeautifulSoup
import urllib.request

limited = 20
url = "https://www.google.co.kr/search?q=%EC%95%84%EC%9D%B4%EC%9C%A0&newwindow=1&safe=strict&sxsrf=ALeKk00eq3WpKxyIYWLL554xWgnSYmnSLg:1625297891531&source=lnms&tbm=isch&sa=X&ved=2ahUKEwim4em7ssbxAhXW73MBHexFCS4Q_AUoAXoECAEQAw&biw=1870&bih=965"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

# imgs = soup.select('img') #select 는 css를 찾는 방식

img = soup.find_all("img", "src")

for i in img:
    
    print(img)
    

# num = 0
# for i in iu_img:
#     num += 1
#     print(i)
#     urllib.request.urlretrieve(i, "./img/", "img" + str(num))
