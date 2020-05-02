import webbrowser
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re

url=input("Enter the url: ")
try:
    html=urllib.request.urlopen(url).read()
except:
    print("Entered url not accessible!!!")
    exit()
soup=BeautifulSoup(html,"html.parser")

for i in soup.find_all(attrs={"href": re.compile("http")}):
            webbrowser.open(i.get("href"))
