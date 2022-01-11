# this program divides a number by another number.

def main():
    # get the numbers to divide.
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    # if num2 is zero and display an error message.
    if num2 != 0:
        # Divide the numbers.
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
    else:
        print("\nThe denominator can't be zero.")

# call the main function.
if __name__ == "__main__":
    main()

    