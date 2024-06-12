####################@@@@@@@@@@@@@@@@@
#simple file
f= open("abc.txt","x")# Creates the specified file,
f.write("Now the file has more content!")
f.close()
f= open("abc.txt")
print(f.read())