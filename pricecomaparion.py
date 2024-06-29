#sample program to compare the prices of two products with the help of web scrapping 
import requests
from bs4 import BeautifulSoup
import re
#product1,url is optional here
url1="https://www.flipkart.com/realme-c55-sunshower-128-gb/p/itm054283d14c56e?pid=MOBGNBYJUA2G5HK4&lid=LSTMOBGNBYJUA2G5HK40FPVVJ&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_bannerads_1_4.bannerAdCard.BANNERADS_A_mobile-phones-store_53EBYE2TQW27&fm=organic&iid=11e8a4fb-c3df-47da-a9aa-d0f0532988cc.MOBGNBYJUA2G5HK4.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=31i7j32h4w0000001680046715511"
obj1=requests.get(url1)
soup1=BeautifulSoup(obj1.content,"html.parser") # here the class is taken from web of that url1 where its user choice
a1=soup1.find("div",class_="_30jeq3 _16Jk6d")
b1=a1.text
c1=re.sub("₹","",b1)
prodprice1=re.sub(",","",c1)
print("price of product 1:-",prodprice1)
prodprice1=int(prodprice1,10)
#product2 ,url is optional here
url2="https://www.flipkart.com/realme-c55-sunshower-64-gb/p/itm054283d14c56e?pid=MOBGNBYJCXN6WRB3&lid=LSTMOBGNBYJCXN6WRB3NDXTAJ&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=b_1_3&otracker=clp_bannerads_1_4.bannerAdCard.BANNERADS_A_mobile-phones-store_53EBYE2TQW27&fm=organic&iid=11e8a4fb-c3df-47da-a9aa-d0f0532988cc.MOBGNBYJCXN6WRB3.SEARCH&ppt=browse&ppn=browse&ssid=31i7j32h4w0000001680046715511"
obj2=requests.get(url2)
soup2=BeautifulSoup(obj2.content,"html.parser")
a2=soup2.find("div",class_="_30jeq3 _16Jk6d") #here the class is taken from web of that url2 where its user choice
b2=a2.text
c2=re.sub("₹","",b2)
prodprice2=re.sub(",","",c2)
print("price of product 2:-",prodprice2)
prodprice2=int(prodprice2,10)

#comaparing
if(prodprice1==prodprice2):
  print("same price")
elif(prodprice1>prodprice2):
  print("product1 price is high than product 2")
else:
  print("product2 price is high than product 1")
