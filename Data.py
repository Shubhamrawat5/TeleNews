import pyfiglet

print("\n")
banner = pyfiglet.figlet_format("WELCOME")
print(banner)


def change():
	r=open("data.txt",'r')

	d=eval(r.readline())
	r.close()
	
	token=d['token']

	print("++++++++++++++++++++++++++++")
	i = input("\nEnter new token (or enter 0 if you dont wanna change previous token): ")

	if(i!='0'):
		token=i
		
	tag = input("\nEnter group chat tag with @ or Enter id: ")
	
	msg =input("\nEnter a message you want to get added in the end of the Tech News (like your channel name or link, if you don't want then just put a space): ")
	
	d["token"]=token
	d["tag"]=tag
	d["msg"]=msg
	
	f=open("data.txt",'w')
	f.write(str(d))

	print("\nToken and chat link/tag and msg saved !")
	print("++++++++++++++++++++++++++++")
	
	f.close()

def display():
	r=open("data.txt",'r')
	print("\n××××××××××××××××××××××××××××")
	print("Current Token and chat link/tag and message:-")
	print(r.readline())
	print("××××××××××××××××××××××××××××")

	r.close()

while(True):
	print("\n--------x-------------------x-----")
	ch=input("1 to change token & chat tag/id & message\n2 to read current token & chat tag/id & message\n0 for exit\nEnter Choice: ")
	if(ch=="1"):
		change()
	elif(ch=="2"):
		display()
	elif(ch=="0"):
		break
	else:
		print("\nIncorrect Choice!! Enter again -\n")