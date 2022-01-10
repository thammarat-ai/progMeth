# This program gets three names from the user and writes them to a file.
def main():
    # Get the names from the user.
    name1 = input('Enter the first name: ')
    name2 = input('Enter the second name: ')
    name3 = input('Enter the third name: ')
    
    # Open the file for writing.
    outfile = open('names.txt', 'w')
    
    # Write the names to the file.
    outfile.write(name1 + '\n')
    outfile.write(name2 + '\n')
    outfile.write(name3 + '\n')
    
    # Close the file.
    outfile.close()
    print('The names have been written to names.txt.')

# Call the main function.
if __name__ == '__main__':
    main()

    
    