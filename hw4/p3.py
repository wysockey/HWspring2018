#Hello fleshy mammal


s=raw_input("Please enter your fav anime")

upper_s = s.upper()

print(upper_s)
lower_s = s.lower()
print(lower_s)

combined =  upper_s + lower_s

print(combined)

num_s = len(s)

print (num_s)

num_combined = len(combined)
print(num_combined)






print(combined)
num_s = len(s)
print (num_s)
num_combined = len(combined)
print (num_combined)

halfway =len(s)/2
print (s[halfway])
print ("at s[0]")
print(s[0])
last = len(s) - 1
print(s[last])
print(s[-1])
firsthalf = s[0:halfway]
lasthalf = s[halfway:last + 1]
print ("this should be first/ last half")
print(firsthalf)
print(lasthalf)


copy = s[:]

skip = s[1::2]
print(skip)

#slice
#start, stop , increment


#concat


value = s[:len(s)/2:-2]
print(value)


print(s.count("1"))

print (s.find("e"))
print (s[:s.find("e")])
replaced = s.replace("great","awesome")

print (replaced)


value = s[len(s) :halfway: -1]
print (value)

words = s.split()
numberofwords = len(words)
print (words[0:2])
print (words[0:2:-1])








