# This program prompts the user to enter the sales amounts
# and writes the amounts to a file.
def main():
    # Get the number of days.
    numDays = int(input("For how many days do you have sales? "))

    # Open a new file named sales.txt.
    salesFile = open("sales.txt", "w")

    # Get the amount of sales for each day.
    # and write the amounts to the file.
    for count in range(1, numDays + 1):
        # Get the sales for a day.
        sales = float(input(f"Enter the sales for day #{count}: "))

        # Write the sales to the file.
        salesFile.write(f"{sales:.2f}\n")

    # Close the file.
    salesFile.close()
    print("Data written to sales.txt")

# call the main function.
if __name__ == "__main__":
    main()

    