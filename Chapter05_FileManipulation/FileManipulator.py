# Creating a file in the 'Files' folder (here in this project) with the 'write' mode
# and writing some text in it
with open("Files/test.txt", "w") as fileW:
    contentW = fileW.write("Test file.")

    # Opening the same file with the 'read' mode
    with open("Files/test.txt", "r") as fileR:
        fileR.read()

        # Opening the same file with the 'read' mode and displaying its content datatype
        # and also displaying the content of the file
        with open("Files/test.txt", "r") as fileRContent:
            contentR = fileRContent.read()
        print("Variable datatype", type(contentR))
        print("\nFile content:\n", contentR)