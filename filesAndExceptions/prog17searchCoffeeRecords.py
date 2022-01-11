# this program allows the user to search for a record in the coffee.txt file.

def main():
    # create a variable to control the loop.
    found = False

    # get the search value.
    search = input("What coffee do you want to find enter description? ")

    # Open the file for reading.
    coffee_file = open("coffee.txt", "r")

    # read the first record's description field.
    descr = coffee_file.readline()

    # read the rest of the file.
    while descr != "" and not found:
        # read the quantity.
        qty = int(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip("\n")

        # Compare the search value with the description.
        if descr == search:
            # Display the data.
            print(f'Description: {descr}')
            print(f'Quantity: {qty}')

            # Set the flag.
            found = True

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

    # If the search value was not found, inform the user.
    if not found:
        print("\nThe search value was not found in the file.")

# Call the main function.
if __name__ == "__main__":
    main()


