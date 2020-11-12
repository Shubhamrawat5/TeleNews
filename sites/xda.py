import requests
from bs4 import BeautifulSoup as bs

def xda():
    url="https://www.xda-developers.com/category/xda-news/"
    response=requests.get(url)
    
    soup=bs(response.content,"html.parser")
    subHtmlBlock=soup.find("div",class_="col main-content col_9_of_12")
    headings=subHtmlBlock.findAll("div",class_="item_content")
    count=0
    
    newsList=[]
    for heading in headings:
        count+=1
        if count==15:
            break
		#if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

        newsList.append("\n\n🌐")
        newsList.append(heading.a.text)

    return newsList