#kristenChing
word = input("Please enter a word. ")
output = ""
length = int(len(word))
for x in range(len(word), 0, -1):
    output = word[0:x]
    print(output)
    
