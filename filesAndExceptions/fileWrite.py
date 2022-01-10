# This program writes all student name data to a file.
def main():
  # Open a file named students.txt
  outfile = open('students.txt')
  
  # Write the names of all students to file
  outfile.write('ARNAN, SANTITHON')
  outfile.write('JAIBANUEAM, CHONTHICHA')
  outfile.write('JAMNAE, AR-PHARAT')
  outfile.write('MOONDENG, WITCHAKORN')
  outfile.write('NADEE, NATTHANICHA')
  outfile.write('NAMDOKMAI, MATAWUT')
  outfile.write('PARAMEE, JIRADET')
  outfile.write('Phollua, Peerawat')
  outfile.write('SOOKAD, THUKDANUY')
  outfile.write('SUKKEAW, PAWORNRAT')
  outfile.write('SUNUNTA, NEERANUCH')
  outfile.write('TIENKAEW, SUNISA')
  outfile.write('WIANGLO, DANAI')
  outfile.write('WONGRIAB, NOPPADOL')
  outfile.write('YAMMEE, CHAWAN')
  
  # Close the file
  outfile.close()
  
# Call the main function
if __name__ == '__main__":
   main()
  
