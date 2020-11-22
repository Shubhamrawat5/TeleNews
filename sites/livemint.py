import requests
from bs4 import BeautifulSoup

def mint():
	url = 'https://www.livemint.com/technology/tech-news'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	div = soup.find("div",class_='listView')
	headings = div.findAll("h2",class_='headline') 

	List = []
	count=0
	for heading in headings:
		news=heading.text
		
		if news[-12:]=="Details here": #slicing news that has "Details here" in the end
			news=news[:-14]

		count=count+1
		
		if count==15:
			break
		#if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

		List.append("\n\n🌐")
		List.append(news)

	return List
