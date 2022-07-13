from bs4 import BeautifulSoup
import requests
import mysql.connector as sql
mycon = sql.connect(host='localhost', user='root', passwd='root', database='test')
cur = mycon.cursor()
source = requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off").text

soup = BeautifulSoup(source,'html.parser')
#print(soup.prettify())
datalist = []
Name = []
price = []
ram = []
InternalStorage = []
Frontcam = []
Rearcam = []
ratings = []
for i in soup.find_all('ul',class_='_1xgFaf'):
     string = i.text
     datalist.append(string.strip())

for i in soup.find_all('div',class_='_4rR01T'):
     string = i.text
     Name.append(string.strip())
for i in soup.find_all('div',class_='_30jeq3 _1_WHN1'):
       price.append(i.text.replace(',','').replace('₹','').strip())


for each in datalist:
           print(each)


# insertSQL = """INSERT INTO scrapedetails (Modelname,price,InternalStorage,frontcam,rearcam)VALUES(%s,%s,%s,%s,%s)"""
# for i in zip(Name,price,datalist,datalist,datalist):
#          cur.execute(insertSQL,i)
#          mycon.commit()
# for i in InternalStorage:
#     cur.execute(insertIS, (i,))
#     mycon.commit()

# for j in price:
#     for k in ram:
     #         for l in InternalStorage:
     #             for m in Frontcam:
     #                 for n in Rearcam:
     #                      cur.execute(insertSQL, (i,j,k,l,m,n,))
     #                      mycon.commit()
print("complete")
#create table sd1(devid int not null auto_increment,modelname varchar(100),