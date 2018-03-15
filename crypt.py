arr1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

arr2=[]
for i in range(len(arr1)):
	arr2.append(arr1[i])

def change_arr2():
	for i in range(keynumber):
		arr2.append(arr2[0])
		arr2.remove(arr2[0])

print("1) Crypt the text")
print("2) Decrypt text")
print("0) Exit \n")

try:

	ans=int(input("Write the number of task:\n[number] > "))

	if ans==1:
		keynumber=int(input("Write encryption key: "))

		change_arr2()
        
		msg=input("\nWrite the text: ")
		msgc=""
		for i in msg:
			for j in range(len(arr1)):
				if i==arr1[j]:
					msgc+=arr2[j]
		print("\nCrypt-text: "+str(msgc))

	elif ans==2:
		keynumber=int(input("Write encryption key: "))

		change_arr2()

		msg=input("\nWrite crypted text: ")
		msgd=""
		for i in msg:
			for j in range(len(arr1)):
				if i==arr2[j]:
					msgd+=arr1[j]
		print("\nDecrypted text: "+str(msgd))
        
	else:
		print("Exit")
        
    

except ValueError:
	print("Error! Print only Integer numbers!")