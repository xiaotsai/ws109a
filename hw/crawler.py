import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.nqu.edu.tw/cht/index.php?") #把此頁面的HTML GET下來
soup = BeautifulSoup(response.text, "html.parser")#用Beautifulsoup4轉為HTML的parser
for k in soup.find_all('a'):
    print(k['href'])#查a標籤的href值
   