# This program uses the for loop to read all of the values in the sales.txt file.

def main():
    # Open the sales.txt file for reading.
    salesFile = open("sales.txt", "r")

    summary = 0

    # Read all the lines from the file.
    for line in salesFile:
        # Convert line to a float.
        amount = float(line)
        # format the amount to display two decimal places.
        print(f"{amount:.2f}")
        summary += amount
    
    # display the total sales.
    print(f"The total sales are ${summary:.2f}")

    
    # Close the file.
    salesFile.close()

# Call the main function.
if __name__ == "__main__":
    main()

    