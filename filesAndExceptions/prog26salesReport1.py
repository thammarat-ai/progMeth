# this program displays the total of the amounts in the sales.txt file.

def main():
    try:
        # inintialize the accumulator.
        total = 0.0

        
        # open the sales.txt file.
        salesFile = open("sales.txt", "r")

        # read the values from the file and accumulate them.
        for line in salesFile:
            amount = float(line)
            total += amount

        # close the file.
        salesFile.close()

        # display the total.
        print("The total of the sales is", format(total, ',.2f'))

    except IOError:
        print("An error occurred trying to read the file.")
    except ValueError:
        print("Non-numeric data in the file.")
    except:
        print("An error occurred.")



# call the main function.
if __name__ == "__main__":
    main()


