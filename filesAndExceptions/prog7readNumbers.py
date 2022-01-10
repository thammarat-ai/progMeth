# this program demonstrates how numbers must be converted from string 
# to integer before they can be used in a calculation.

def main():
    # open the file for reading.
    infile = open('numbers.txt', 'r')

    # read the first three lines from the file.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # close the file.
    infile.close()

    # add the three numbers.
    total = num1 + num2 + num3

    # display the total.
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'The total is: {total}')

# Call the main function.
if __name__ == '__main__':
    main()



    