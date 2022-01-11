# this program displays the contents of a file.

def main():
    # get the name of the file to read.
    filename = input("Enter the name of the file: ")
    infile = open(filename, 'r')
    # read the contents of the file.
    contents = infile.read()
    # display the contents.
    print(contents)
    infile.close()

# call the main function.
if __name__ == "__main__":
    main()

    