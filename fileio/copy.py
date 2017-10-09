
file=open("file.txt","r")
fileToWriteTo=open("copy.txt","w")
fileToWriteTo.write(file.read())
file.close()
fileToWriteTo.close()
