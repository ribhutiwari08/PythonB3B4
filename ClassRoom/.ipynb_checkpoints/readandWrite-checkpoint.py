#create file handle
file = open("example.txt", "w")
#write data  in file
file.write("Hello , this is a test ")
#save and close file
file.close()

#add new line in the existing file
file = open("example.txt", "a")
file.write("\n new line " .upper())
file.close()

#for reading the data 
filename = "example.txt"
file = open(filename, "r")

fileContent = file.readlines()
file.close()

print(fileContent)

