# This program reads a file 'student.txt' one line at a time.
def main():
    # Open the file for reading.
    infile = open('students.txt', 'r')

    # Read the first 5 lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()

    # Strip the newline characters from the lines.
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    line4 = line4.rstrip('\n')
    line5 = line5.rstrip('\n')

    # Close the file.
    infile.close()

    # Print the lines.
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

# Call the main function.
if __name__ == '__main__':
    main()

    
