import requests
from bs4 import BeautifulSoup

def today():
	url1 = 'https://www.indiatoday.in/technology/news'
	page = requests.get(url1)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='catagory-listing')
	#print(cl)
	List = []
	count=0
	
	for i in cl:
		Y=i.find("h2")
		#z=Y.get_text()
		#print(z)
		count=count+1
		List.append("\n\n🌐")
		List.append(Y.get_text())	
		
	List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")
	
	url= 'https://www.indiatoday.in/technology/news?page=1'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='catagory-listing')
	
	for i in cl:
		Y=i.find("h2")
		#z=Y.get_text()
		#print(z)
		count=count+1
		if(count==18):
			break

		List.append("\n\n🌐")
		List.append(Y.get_text())
	#print(List)
	return List