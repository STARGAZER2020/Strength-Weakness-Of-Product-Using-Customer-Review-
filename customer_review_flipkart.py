from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
import requests
import time

def read_file():
   file=open("file.html")
   data = file.read()
   file.close()
   return data

main_url = "https://www.flipkart.com/redmi-note-7-pro-nebula-red-64-gb/product-reviews/itmferghuf9ky6ru?pid=MOBFDXZ3UJJ7ETTE"

main_url = main_url+'&page='
url = main_url

user_agent = UserAgent()

for i in range(1,60):
  
   url=main_url
   url = url + str(i)
   print(url)
   page = requests.get(url,headers={'user-agent':user_agent.chrome})
   soup = BeautifulSoup(page.content,'lxml')

   review = soup.find('div',class_='_1HmYoV _35HD7C col-9-12').find_all('div',class_="qwjRop")

   review = [ tags.div.div.string for tags in review]
   time.sleep(30)
	
'''   head_review = soup.find('div',class_='_1HmYoV _35HD7C col-9-12').find_all('p',class_='_2xg6Ul')


   for tags in head_review:
      print(tags.string)

   print("")
   print("")'''

'''   rating = soup.find('div',class_='_1HmYoV _35HD7C col-9-12').find_all('div',class_='hGSR34 E_uFuv')

   for ratings in rating:
      print(ratings.contents[0])'''

count=0

for reviews in review:
   if( reviews is not None):
      count+=1

print(count)
      
