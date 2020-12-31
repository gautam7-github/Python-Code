from os import walk

direc = r"C:\Users\91978\Desktop\test"
tree = walk(direc)

for folder, subfolder, filename in tree:
    print(f"{folder} TOP LEVEL")
    tree2 = walk(folder)
    for folder, subfolder, filename in tree2:
        print(folder, subfolder, filename)
