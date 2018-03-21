s = input("Please enter a sentence: ")
cap = []
out = []
for word in s.split():
    if word.islower():
        out.append(word)
    else:
        cap.append(word)

onelist = withcap + without

for word in onelist:
    print (word)

uin = input("Enter your text: ")

## hold lower case/upper case words
up_words = []
no_up_words = []

for i, word in enumerate(uin.strip().split()):
    if word.islower():
        no_up_words.append(word)
    else: 
        up_words.append(word)

print( up_words, no_up_words)




