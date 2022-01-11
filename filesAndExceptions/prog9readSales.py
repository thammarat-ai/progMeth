# This program reads all of the values in sales.txt
def main():
    # Open the sales.txt file for reading.
    salesFile = open("sales.txt", "r")

    # Read the first line from the file,
    # but don't convert to a number.
    # We still need to test for an empty string.
    line = salesFile.readline()

    # as long as an empty string is not returned,
    # keep reading lines.
    while line != "":
        # Convert the line to a float.
        amount = float(line)

        # format the amount to display two decimal places.
        print(f"{amount:.2f}")

        # Read the next line.
        line = salesFile.readline()

    # Close the file.
    salesFile.close()
# Call the main function.
if __name__ == "__main__":
    main()

    