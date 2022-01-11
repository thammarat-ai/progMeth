# This program displays the records in the file employeeData.txt.

def main():
    # Open the file for reading.
    emp_file = open("employeeData.txt", "r")

    # Read the file's contents.
    name = emp_file.readline()

    # if a file is empty, contents will be an empty string.
    while name != "":
        # read the ID number 
        id_num = emp_file.readline()

        # read the department
        dept = emp_file.readline()

        # Strip the newline characters from the end of the string.
        name = name.rstrip("\n")
        id_num = id_num.rstrip("\n")
        dept = dept.rstrip("\n")

        # Display the data.
        print(f'Name: {name}')
        print(f'ID number: {id_num}')
        print(f'Department: {dept}')
        print()

        # Read the next name.
        name = emp_file.readline()

    # Close the file.
    emp_file.close()

# Call the main function.
if __name__ == "__main__":
    main()

