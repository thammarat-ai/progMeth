# this program displays the total of the amounts in the sales.txt file.

def main():
    try:
        # inintialize the accumulator.
        total = 0.0

        
        # open the sales.txt file.
        salesFile = open("sales2.txt", "r")

        # read the values from the file and accumulate them.
        for line in salesFile:
            amount = float(line)
            total += amount

        # close the file.
        salesFile.close()

        # display the total.
        print("The total of the sales is", format(total, ',.2f'))

    except:
        print("An error occurred.")



# call the main function.
if __name__ == "__main__":
    main()


