num = 0
words = []
distinct = []

num = input()

for i in range(int(num)):
    words.append(input())
    
mydict = dict()


for word in words:
    if word in mydict:
        mydict[word] = str(int(mydict[word]) + 1)
    else:
        mydict[word] = str(1)
        
print(len(mydict))

print(" ".join(list(mydict.values())))
