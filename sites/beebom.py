import requests
from bs4 import BeautifulSoup

def bom():
    url = 'https://beebom.com/category/news/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    headings = soup.findAll("div",class_='item-details')

    count=0
    List = []
	
    count=0 #to get only top 14 news
    for heading in headings:
        news=heading.a.text

        if news[:4]=="This" or news[:5]=="These" or news[-3:]=="...": #filter heading that start with This,These and which end with ...
            continue

        count+=1

        if count==15:
            break
        #if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
        
        List.append("\n\n🌐")
        List.append(news)
	
    return List