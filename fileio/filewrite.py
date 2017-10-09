file=open("file.txt","w")

file.write("This is writing to file")
file.close()

fileAppend=open("file.txt","a")
fileAppend.write("This is appending")
