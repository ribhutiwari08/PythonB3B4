import pickle

with open("readData.pickle" , "rb") as file:
    loaded_data = pickle.load(file)

print("Deserialized data:" , loaded_data)