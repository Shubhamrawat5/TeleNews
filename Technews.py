import requests
from bs4 import BeautifulSoup
import telebot # pyTelegramBotAPI library

f=open("data.txt",'r')
data=f.readline()
data=eval(data)
bot_token=data["token"]
chat_tag=data["tag"]

bot = telebot.TeleBot(token=bot_token)

site=input("Enter 1 to get Technews from GadgetsNdtv\nEnter 2 to get TechNews from LiveMint\nEnter Choice:-")
if(site=='1'):
	url = 'https://gadgets.ndtv.com/news'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='news_listing')
	
elif(site=='2'):
	url = 'https://www.livemint.com/technology/tech-news'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='headlineSec')

else:
	print("\nWrong Choice! Exit")
	exit()

#print(cl)
count =0
List = []
for i in cl:
	count=count+1

	#print(i.text)
	List.append("\n\n🌐")
	List.append(i.text)
	if(count==15):
		break
	if(count==11):
		List.append("\n🌐 Join @pvxtechnews for daily tech news !")

List.insert(0,'☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆')
#print(List)
text = " ".join(List)
print(text)

print("\n------------------------")
ch=input(f"ENTER 1 TO SEND ABOVE TECH NEWS TO GROUP LINK TAG: {chat_tag} or ENTER ANY OTHER CHARACTER NOT TO SEND! :")
if(ch=='1'):
	try:
		bot.send_message(chat_tag,text)
		print("\nTECH NEWS POSTED :) !!")
	except:
		print("Something is wrong!!!!!!! (maybe token or chat link tag is not correct!")

else:
		print("\nNot Posted :( !!")
		
f.close()