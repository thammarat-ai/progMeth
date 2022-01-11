# This programm gets employee data from the user and saves it to a file.
# employeeData.txt
def main():
    # Get the employee data.
    num_employees = int(input("How many employees will be processed? "))

    # Open a file for writing.
    emp_file = open("employeeData.txt", "w")

    # Get each employee's data and write it to the file.
    for count in range(1, num_employees + 1):
        # Get the data for the employee.
        print("Enter data for employee #", count, sep="")
        emp_name = input("Name: ")
        emp_id = input("ID number: ")
        emp_dept = input("Department: ")
        

        # Write the data to the file.
        emp_file.write(f'{emp_name}\n')
        emp_file.write(f'{emp_id}\n')
        emp_file.write(f'{emp_dept}\n')

        # Display a blank line.
        print()
    # Close the file.
    emp_file.close()
    print("Employee data written to employeeData.txt")

# Call the main function.
if __name__ == "__main__":
    main()

    
        