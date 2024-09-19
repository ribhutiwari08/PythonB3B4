
#Opening a file for reading (with 'with')
with open("testdata.csv", "r") as file:
    content = file.read()   # Reading the content
    print(content)   # Displaying the content the file 


    rows = content.split("\n")
    for row in rows:
        print(f"row is {row}")
        cols = row.split(",")
        for col in cols:
            print(col)

