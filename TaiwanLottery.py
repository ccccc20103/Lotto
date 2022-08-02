import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select("#rightdown")
#print(data1)

data2 = data1[0].find('div', {'class':'contents_box01'})
#print(data2)

data3 = data2.find_all('div', {'class':'ball_tx ball_yellow'})
##print(data3)
#
# BINGO號碼

print("\nBINGO號碼：",end="")  
for n in range(0,20):
    print(data3[n].text,end="  ") 

red = data2.find('div', {'class':'ball_red'})     
print("\n超級獎號：{}".format(red.text)) 