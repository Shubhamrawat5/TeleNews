import requests
from bs4 import BeautifulSoup

def zee():
	url = 'https://zeenews.india.com/technology'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page = requests.get(url, headers=headers)

	#page = requests.get(url) site is not allowing web scrapers to using headers

	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup)

	headings = soup.findAll(class_='sec-con-box')

	count=0
	List = []
	for heading in headings:
		count=count+1

		if count==15:
			break
		#if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

		List.append("\n\n🌐")
		List.append(heading.h3.a.text)

	return List
	