#Kristen Ching
word = input("Please enter a word. ")
output = ""
length = int(len(word))
for i in range(0, length, 1):
    output = word[length - i: length]
    print(output)
