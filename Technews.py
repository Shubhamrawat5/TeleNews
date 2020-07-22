import requests
from bs4 import BeautifulSoup
from sites import (gadgetsndtv,livemint,indiatoday)
import telebot # pyTelegramBotAPI library

f=open("data.txt",'r')
data=f.readline()
data=eval(data)
bot_token=data["token"]
chat_tag=data["tag"]
f.close()

bot = telebot.TeleBot(token=bot_token)

site=input("\n[Note: GadgetsNdtv is best]\nEnter 1 to get Technews from GadgetsNdtv\nEnter 2 to get TechNews from LiveMint\nEnter 3 to get Technews from IndiaToday\nEnter Choice:-")

if(site=='1'):
	List=gadgetsndtv.ndtv()
	
elif(site=='2'):
	List=livemint.mint()
	
elif(site=='3'):
	List=indiatoday.today()
	
else:
	print("\nWrong Choice! Exit")
	exit()

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
		