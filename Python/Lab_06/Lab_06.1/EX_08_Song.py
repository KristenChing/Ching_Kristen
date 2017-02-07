#Kristen Ching
def sing(word, num):
    global output
    output = ""
    for x in range(0, num):
            output = output + word + " "
            if x == (num - 1):
                print(output)
sing("Na", 4)
sing("Na", 4)
sing("Hey", 3)
sing("Goodbye!", 1)

