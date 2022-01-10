# this program demonstrates how numbers must be converted to strings before they can be written to a file.
def main():
    # Open the file for writing.
    outfile = open('numbers.txt', 'w')

    # Get three numbers from the user.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter a final number: '))

    # Write the numbers to the file.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Close the file.
    outfile.close()
    print('The numbers have been written to numbers.txt.')

# Call the main function.
if __name__ == '__main__':
    main()

