# this program calculates the gross pay for an employee

def main():
    try:
        # get the number of hours worked and the hourly pay rate.
        hours = int(input("Enter the number of hours worked: "))
        rate = float(input("Enter the hourly pay rate: "))
        
        # calculate the gross pay.
        grossPay = hours * rate
        
        # display the gross pay.
        print("The gross pay is $", format(grossPay, ',.2f'), sep='')
    except ValueError as err:
        print(err)


# call the main function.
if __name__ == "__main__":
    main()

    