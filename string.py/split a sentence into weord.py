str=input("enter sentence...>")
words=[]
word=" "
for i in str:
    if i!=" ":
        word+=i
    else:
        words.append(word)
        word=" "
if word!=" ":
    words.append(word)
print(words)