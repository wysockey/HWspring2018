s=raw_input("Write a Sentence. ")
halfway =len(s)/2
print (s[halfway])
print ("at s[0]")

last = len(s) - 1
print(s[last])
print(s[-1])
firsthalf = s[0:halfway]
lasthalf = s[halfway:last ]
print ("this should be first/ last half")
print(firsthalf)
print(lasthalf)

