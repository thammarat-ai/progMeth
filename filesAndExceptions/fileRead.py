# This program reads and displays th contents of the students.txt file.
def main():
  # Open a file name students.txt
  infile = open('students.py')
  
  # Read th file's data
  fileData = infile.read()
  
  # Close the file.
  infile.close()
  
  # Print the data that was read into memory
  print(fileData)
  
# Call the main function
if __main__ == '__main__':
  main()
