#Kristen Ching
word = input("Please enter a word. ")
output = ""
length = len(word)
for i in range(0, length, 1):
    output = word[i: length]
    print(output)
