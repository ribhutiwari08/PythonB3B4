# write a program to save a python list object in to a file and then read the same object as list
import pickle

list1=[1,2,3,4]

filePath = "data.txt"

with open(filePath,"w") as  fileHandle:
    fileHandle.write(str(list1))

with open(filePath, "r") as fileHandle:
    readData = fileHandle.read()
    readData = readData[1:len(readData)-1].replace(" ","").split(",")
    print(f"read data is{readData} \n its type is {type(readData)}")

with open("readData.pickle" , "wb") as file:
    pickle.dump(readData,file)

print("Data has been serialized and saved to data.pickle")