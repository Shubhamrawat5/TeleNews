import requests
from bs4 import BeautifulSoup

def zee():
	url = 'https://zeenews.india.com/technology'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page = requests.get(url, headers=headers)

	#page = requests.get(url)

	#print(page)
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup)
	cl = soup.findAll(class_='sec-con-box')

	#print(cl)
	List = []
	for i in cl:
		#print(i.text)
		x=i.text.find("\n\n\n")
		#print(x)
		List.append("\n\n🌐")
		List.append(i.text[3:x])

	return List
	