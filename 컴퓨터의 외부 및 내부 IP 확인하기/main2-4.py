import socket
import requests
import re
from bs4 import BeautifulSoup


in_addr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr",443))
print("내부 IP : ",in_addr.getsockname()[0])

req= requests.get("http://ipconfig.kr")
req.encoding = req.apparent_encoding

soup = BeautifulSoup(req.text,"html.parser")

ip_td = soup.find('th', string="IP 주소")
if ip_td and ip_td.find_next_sibling("td"):
    out_addr = ip_td.find_next_sibling("td").text.strip()
    print("외부 iP : ",out_addr)
else:
    print("외부 IP 주소를 찾을 수 없습니다.")
