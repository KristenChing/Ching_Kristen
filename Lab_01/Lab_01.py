import time
ASCII_art = open("mountain_ASCII_art.txt","r")
count = 0
while (count < 6):
    line = ASCII_art.readline()
    count+=1
    time.sleep(1)
    print (line)
