#Kristen Ching
sentence = input("Please enter a sentence. ")
def replace(sentence):
    if " " not in sentence:
        return sentence
    else:
        return replace(sentence.replace(" ", "_"))
print(replace(sentence))
