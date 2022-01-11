# This program displays the records in the coffee.txt file.

def main():
    # Open the file for reading.
    coffee_file = open("coffee.txt", "r")

    # read the first record's description field.
    descr = coffee_file.readline()
    
    # read the rest of the file.
    while descr != "":
        # read the quantity.
        qty = int(coffee_file.readline())
        
        # Strip the \n from the description.
        descr = descr.rstrip("\n")
        
        # Display the data.
        print(f'Description: {descr}')
        print(f'Qunantity: {qty}')
        
        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

# Call the main function.
if __name__ == "__main__":
    main()

    