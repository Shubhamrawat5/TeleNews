import requests
from bs4 import BeautifulSoup
import telebot # pyTelegramBotAPI library

f=open("data.txt",'r')
data=f.readline()
data=eval(data)
bot_token=data["token"]
chat_id=int(data["id"])
chat_tag=data["tag"]

bot = telebot.TeleBot(token=bot_token)
url = 'https://gadgets.ndtv.com/news'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
cl = soup.findAll(class_='news_listing')
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
	#if(count==11):
		#List.append("\n🌐 Join @pvxtechnews for daily tech news !")

List.insert(0,'☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆')
#print(List)
text = " ".join(List)
print(text)

ch=int(input(f"ENTER WHERE TO SEND! \n1 to send in chat id: {chat_id} \n2 to send in chat link tag: {chat_tag}\nEnter choice: "))
if(ch==1):
	try:
		bot.send_message(chat_id,text)
		print("TECH NEWS POSTED !")
	except:
		print("Something is wrong!!!!!!! (maybe token or chat id is not correct!")
		
elif(ch==2):
	try:
		bot.send_message(chat_id,text)
		print("TECH NEWS POSTED !")
	except:
		print("Something is wrong!!!!!!! (maybe token or chat link tag is not correct!")
		
f.close()