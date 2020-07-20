def change():
	d={}
	w=open("data.txt",'w')
	print("++++++++++++++++++++++++++++")
	token = input("Enter token: ")
	id = input("Enter group/channel/user id: ")
	tag= input("Enter group tag with @: ")
	d["token"]=token
	d["id"]=id
	d["tag"]=tag
	w.write(str(d))

	print("\nToken and ID saved and chat tag saved !")
	print("++++++++++++++++++++++++++++")
	
	w.close()

def display():
	r=open("data.txt",'r')
	print("××××××××××××××××××××××××××××")
	print("Current Token and id and chat tag:-")
	print(r.readline())
	print("××××××××××××××××××××××××××××")

	r.close()

while(True):
	print("\n--------x-------------------x-----")
	ch=input("1 to change token & id & chat tag\n2 to read current token & id & chat tag\n0 for exit\nEnter Choice: ")
	if(ch=="1"):
		change()
	elif(ch=="2"):
		display()
	elif(ch=="0"):
		break
	else:
		print("\nIncorrect Choice!! Enter again -\n")