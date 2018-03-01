


#Homework  1.0 attempt 29

number = int(raw_input("What is the tempeture"))
Yes = ("Yes")
No = ("No")
if(number >= 99.0): 
	print("You feeling warm bud?")
	Yah = raw_input()
	if ("Yes" ==  "yes"): 
		print("you may be running a fever")
	Nay = raw_input()
	if ("No" == "no"): 
		print("You must be warm blooded.")
elif(number =< 96.0):
	print("Are you feeling cold bud?")
	cancer = raw_input()
	if("Yes" == "yes"):
		print("Trying dress up for winter to keep your temperature up!")
	dank= raw_input()
	if ("No" == "no"):
		print("How high are you to be not that cold? You must be cold blooded....")
elif(number = 98.6):
	print("Congratulations, you are normal and healthy!")  	
elif(96.0 < number <98.6):
	print ("Your somewhat normal in tempeture!")
elif(98.6 < number < 99.0):
	print("Your still somewhat normal in tempeture!")
