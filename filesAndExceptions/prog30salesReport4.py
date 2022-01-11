# this program displays the total of the amounts in the sales.txt file.

def main():
    total = 0.0
    try:
        # open the sales.txt file.
        salesFile = open("sales.txt", "r")

        # read the values from the file and accumulate them.
        for line in salesFile:
            amount = float(line)
            total += amount

        # close the file.
        salesFile.close()
    except Exception as err:
        print(err)
    finally: #else:
        # display the total.
        print("The total of the sales is", format(total, ',.2f'))



# call the main function.
if __name__ == "__main__":
    main()


