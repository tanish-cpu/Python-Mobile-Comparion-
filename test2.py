from bs4 import BeautifulSoup
import requests
import mysql.connector as sql
mycon = sql.connect(host='localhost', user='root', passwd='root', database='test')
cur = mycon.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
source = requests.get("https://www.amazon.in/apple-iphone-mobile/s?k=apple+iphone+mobile",headers = headers).text

soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())

Name = []
price = []
ram = []
for i in soup.find_all('span',class_='a-size-medium a-color-base a-text-normal'):
     string = i.text
     Name.append(string.strip())

for i in soup.find_all('span',class_='a-price-whole'):
       price.append(i.text.replace(',','').replace('₹','').strip())


for each in Name:
         print(each)
insertSQL = """INSERT INTO scrapedetails (modelname,price)VALUES(%s,%s)"""
for i in Name:
    for j in price:
        cur.execute(insertSQL, (i,j,))
        mycon.commit()
print("complete")
