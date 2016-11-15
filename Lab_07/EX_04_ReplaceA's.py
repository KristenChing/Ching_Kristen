#Kristen Ching
sentence = input("Please enter a sentence. ")
def replace():
        global sentence
        while "a" in sentence:
                sentence = sentence.replace("a", "@")
        return(sentence)
print(replace())
