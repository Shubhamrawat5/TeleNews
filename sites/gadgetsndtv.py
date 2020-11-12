import requests
from bs4 import BeautifulSoup

def ndtv():
	url = 'https://gadgets.ndtv.com/news'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	headings = soup.findAll(class_='news_listing')
	
	List = []
	count=0 #to get only top 15 news
	for heading in headings:
		#print(i.text)
		count=count+1
		
		if count==15:
			break
		#if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

		List.append("\n\n🌐")
		headline=heading.text

		if headline[-23:]==": Price, Specifications": #cropping headlings having this text in the end
			List.append(headline[:-23])
		else:
			List.append(headline)
	return List
