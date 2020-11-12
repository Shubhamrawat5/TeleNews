import requests
from bs4 import BeautifulSoup

def express():
	url = "https://indianexpress.com/section/technology"
	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')
	
	div=soup.find("div",class_='top-article')
	headings=div.findAll("li")
	
	count=0
	List = []
	
	for heading in headings:
		count+=1
		if count==15:
			break

		#if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
		
		List.append("\n\n🌐")
		List.append(heading.h3.a.text)

	return List
	