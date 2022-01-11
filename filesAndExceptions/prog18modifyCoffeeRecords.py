# This program allows the user to modify the quantity of a record in the coffee.txt file.

import os

def main():
    # create a variable to control the loop.
    found = False

    # get the search value.
    search = input("What coffee do you want to find enter description? ")
    new_qty = int(input("What is the new quantity? "))

    # Open the file for reading.
    coffee_file = open("coffee.txt", "r")

    # Open the temporary file.
    temp_file = open("temp.txt", "w")

    # read the first record's description field.
    descr = coffee_file.readline()

    # read the rest of the file.
    while descr != "" and not found:
        # read the quantity.
        qty = int(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip("\n")

        # write either this record to the temp file
        # or the new record to the temp file
        if descr == search:
            # write the new record to the temp file
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')
            found = True
        else:
            # write this record to the temp file
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file.
    os.remove("coffee.txt")

    # Rename the temporary file.
    os.rename("temp.txt", "coffee.txt")

    # if the search value was not found, inform the user.
    if not found:
        print("\nThe search value was not found in the file.")
    else:
        print("\nThe quantity was updated.")


# Call the main function.
if __name__ == "__main__":
    main()

    
