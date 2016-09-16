import time
ASCII_art=open("flower_ASCII_art.txt","r")
count = 0
while count < 13:
    line = ASCII_art.readline()
    print (line)
    time.sleep(1)
    count +=1

               
