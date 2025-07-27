import requests
import re
from bs4 import BeautifulSoup



req = requests.get("http://ipconfig.kr/")
req.encoding = req.apparent_encoding
soup = BeautifulSoup(req.text, "html.parser")

ip_td = soup.find('th', string="IP 주소")
if ip_td and ip_td.find_next_sibling("td"):
    out_addr = ip_td.find_next_sibling("td").text.strip()
    print("IP 주소:", out_addr)
else:
    print("IP 주소를 찾을 수 없습니다.")
