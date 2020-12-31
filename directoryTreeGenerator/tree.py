from os import walk


tree = walk(r"C:\Users\91978\Desktop\test")

for folder, subfolder, filename in tree:
    print(f"{folder} TOP LEVEL")
    for i in subfolder:
        print(i, " SUB FOLDER")
    for j in filename:
        print(j, "FILES")
