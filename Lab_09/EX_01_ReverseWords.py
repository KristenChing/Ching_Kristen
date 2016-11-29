#Kristen Ching
words = ["hi", "I", "am", "a", "cat"]
print("In order...")
for word in words:
    print(word)
print("\n")
print("In reverse...")
def reverse(words):
    for i in range(len(words)-1, -1, -1):
        print(words[i])
reverse(words)
