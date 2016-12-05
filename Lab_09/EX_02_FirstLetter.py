#Kristen Ching
words = ["hello", "pie", "apple", "cat", "omonomonomonomonom"]
output = ""
def first(words):
    global output
    for i in words:
        output += i[0]
    return output
print(first(words))
first(words)
