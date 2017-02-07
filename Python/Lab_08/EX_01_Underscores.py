#Kristen Ching
sentence = input("Please enter a sentence. ")
def replace(sc):
    if " " not in sc:
        return sc
    else:
       return sc[0:sc.index(" ")] + "_" + replace(sc[sc.index(" ")+1:len(sc)])

print(replace(sentence))
