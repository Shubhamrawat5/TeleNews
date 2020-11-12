import requests
from bs4 import BeautifulSoup

def today():
	url = 'https://www.indiatoday.in/technology/news'
	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')
	headings = soup.findAll(class_='catagory-listing')

	List = []
	count=0
	
	for heading in headings:
		count=count+1

		if count==15:
			break
		#if count==11:
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

		List.append("\n\n🌐")
		List.append(heading.a.text)	
		
	return List