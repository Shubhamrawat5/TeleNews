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
        count+=1

        if count==15:
            break
        #if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
        
        List.append("\n\n🔅")
        List.append(heading.a.text)
	
    return List