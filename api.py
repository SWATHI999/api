from flask import Flask,redirect
import bs4 as bs
import urllib
import requests
import json
app = Flask(__name__)

@app.route('/get_price/<string:name>')
def index(name):
   return redirect('/'+name)
@app.route('/flipkart')
def flipkart():
   flip={}
   data=urllib.urlopen('https://www.flipkart.com/vivo-v9-pearl-black-64-gb/p/itmf3k77fmxzaph9?pid=MOBF3J4H2XT7QRUG&srno=s_1_2&otracker=search&lid=LSTMOBF3J4H2XT7QRUGXXCDK3&fm=SEARCH&iid=81f3db94-a110-4d7c-bcbb-821d2463073e.MOBF3J4H2XT7QRUG.SEARCH&ppt=Search%20Page&ppn=Search%20Page&ssid=8rk85930l1q0tji81521976390869&qH=eb4af0bf07c16429')
   retd=bs.BeautifulSoup(data,"lxml")
   flip['product_Name']=retd.find("h1",{"class":"_3eAQiD"}).text
   flip['price']=retd.find("div", {"class": "_1vC4OE _37U4_g"}).text
   if retd.find("div",{"class":"_3HGjxn"}).a.text:
   	flip['seller']=retd.find("div",{"class":"_3HGjxn"}).a.text
   else:
	flip['seller']="no seller"
   return json.dumps(flip)
@app.route('/amazon')
def amazon():
   ama={}
   data=urllib.urlopen('https://www.amazon.in/Trase-Flint-Black-Sandal-Dailywear-5/dp/B073VPRRNT/ref=sr_1_4?s=shoes&rps=1&ie=UTF8&qid=1521977395&sr=1-4&keywords=PrimeTraseFashionFootwear&refinements=p_85%3A10440599031%2Cp_6%3AA1KWBFV2WLTE9U')
   retd=bs.BeautifulSoup(data,"lxml")
   ama['product_name']=retd.find("span",{"class":"a-size-large"}).text
   ama['price']=retd.find("span", {"class": "a-size-medium a-color-price"}).text
   if retd.find("li",{"id":"SalesRank"}).text:
   	st=retd.find("li",{"id":"SalesRank"}).text
        in1=st.split('#')
        in2=in1[1].split('\n')
        ama['seller_id']=in2[0]
   else:
	ama['seller_id']="no seller"
   return json.dumps(ama)
@app.route('/myntra')
def myntra():
  return 'myntra'
if __name__ == '__main__':
   app.run()
