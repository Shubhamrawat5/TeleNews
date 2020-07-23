import requests
from bs4 import BeautifulSoup

def mint():
	url = 'https://www.livemint.com/technology/tech-news'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='headlineSec')
	
	List = []
	count=0
	for i in cl:
		#print(i.text)
		count=count+1
		if(count==15):
			break
		#if(count==11):
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

		List.append("\n\n🌐")
		if(i.text[-4:]=="2020"):
			List.append(i.text[:-24])
		else:
			List.append(i.text[:-25])
	return List
