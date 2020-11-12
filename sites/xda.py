import requests
from bs4 import BeautifulSoup as bs

def xdaa():
    url="https://www.xda-developers.com/category/xda-news/"
    response=requests.get(url)
    
    soup=bs(response.content,"html.parser")
    subHtmlBlock=soup.find("div",class_="col main-content col_9_of_12")
    headings=subHtmlBlock.findAll("div",class_="item_content")
    count=0
    
    newsList=[]
    for heading in headings:
        count+=1
        newsList.append("\n\n🌐")
        newsList.append(heading.a.text)
        if count==15:
            break
   
   return newsList
 