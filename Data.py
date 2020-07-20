def change():
	r=open("data.txt",'r')

	d=eval(r.readline())
	r.close()
	
	token=d['token']

	print("++++++++++++++++++++++++++++")
	i = input("Enter new token (or enter 0 if you dont wanna change previous token): ")

	if(i!='0'):
		token=i
		
	tag = input("Enter group chat link/tag with @: ")
	d["token"]=token
	d["tag"]=tag
	
	f=open("data.txt",'w')
	f.write(str(d))

	print("\nToken and chat link/tag saved !")
	print("++++++++++++++++++++++++++++")
	
	f.close()

def display():
	r=open("data.txt",'r')
	print("\n××××××××××××××××××××××××××××")
	print("Current Token and chat link/tag:-")
	print(r.readline())
	print("××××××××××××××××××××××××××××")

	r.close()

while(True):
	print("\n--------x-------------------x-----")
	ch=input("1 to change token & chat link/tag\n2 to read current token & chat link/tag\n0 for exit\nEnter Choice: ")
	if(ch=="1"):
		change()
	elif(ch=="2"):
		display()
	elif(ch=="0"):
		break
	else:
		print("\nIncorrect Choice!! Enter again -\n")