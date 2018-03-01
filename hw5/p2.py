#Any number ending with 0,2,4,6,8

#Amount of people you have to feed in communist countries/Socialist countries through  bread lines/


Number = int(input("Enter a number!"))
flag = Number%2

NumberDank = Number* 3 + 1

if flag  ==0:
	print(NumberDank, "is an even number.")
elif flag == 1:
	print(NumberDank," is an odd number")
else:
	print("Error, Invalid input")

