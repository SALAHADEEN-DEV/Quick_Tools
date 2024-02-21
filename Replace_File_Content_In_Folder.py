import os

path = input("Enter a path: ")
extension = input("Enter a extension default (dart): ")
remove = input("Enter the string to be removed: ")
replace = input("Enter the string to be replaced: ")

if extension == '':
    extension = 'dart'
    
for path, subdirs, files in os.walk(path):
    for name in files:
        file=str(os.path.join(path, name))

        if extension in file:
            # Read in the file
            with open(file, "r") as file:
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace(remove,replace)
            
            # re type the name agin
            file=file.name
            
            # Clear Content
            open(file, 'w').close()

            # Write the file out again
            with open(file, "w") as file:
                file.write(filedata)
