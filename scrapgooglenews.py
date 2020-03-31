#Rumil Shah
#This code web scrapes news from GoogleNews website and returns Headline, Link and publish Date

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

for i in news_list:
  print("NEWS TITLE : \n"+i.title.text+"\n")
  print("LINK : ")
  print(i.link.text+"\n")
  print("PUBLISH DATE :\n "+i.pubDate.text+"\n")
  print("-"*50+"\n")

