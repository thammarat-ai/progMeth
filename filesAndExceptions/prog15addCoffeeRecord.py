# This program adds coffee inventory recored to the file coffee.txt.

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the file for appending.
    coffee_file = open("coffee.txt", "a")

    # add records to the file.
    while another == 'y' or another =='Y':
        # Get the coffee data from the user.
        print("Enter the coffee data: ")
        descr = input("Coffee description: ")
        qty = int(input("Number in pounds: "))

        # Append the data to the file.
        coffee_file.write(descr +'\n')
        coffee_file.write(f'{qty}\n')

        # Determine whether the user wants to enter another record.
        print("Enter another record? (y/n)")
        another = input()

    # Close the file.
    coffee_file.close()

# Call the main function.
if __name__ == "__main__":
    main()

    

        