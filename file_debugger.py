try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except:
    print("File not found")
