import requests
from bs4 import BeautifulSoup

url = "https://www.google.co.kr/search?q=%EC%95%84%EC%9D%B4%EC%9C%A0&newwindow=1&safe=strict&sxsrf=ALeKk00eq3WpKxyIYWLL554xWgnSYmnSLg:1625297891531&source=lnms&tbm=isch&sa=X&ved=2ahUKEwim4em7ssbxAhXW73MBHexFCS4Q_AUoAXoECAEQAw&biw=1870&bih=965"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

picture = soup.find_all("div", {"class": "bRMDJf islir"}, limit = 20)

print(picture)