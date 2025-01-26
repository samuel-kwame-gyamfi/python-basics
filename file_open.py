try:
    open_file = input("Enter file name: ")
    with open(open_file,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")