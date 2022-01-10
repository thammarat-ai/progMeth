# This program writes all student name data to a file.
def main():
  # Open a file named students.txt
  outfile = open('students.txt','w')
  
  # Write the names of all students to file
  outfile.write('ARNAN, SANTITHON\n')
  outfile.write('JAIBANUEAM, CHONTHICHA\n')
  outfile.write('JAMNAE, AR-PHARAT\n')
  outfile.write('MOONDENG, WITCHAKORN\n')
  outfile.write('NADEE, NATTHANICHA\n')
  outfile.write('NAMDOKMAI, MATAWUT\n')
  outfile.write('PARAMEE, JIRADET\n')
  outfile.write('Phollua, Peerawat\n')
  outfile.write('SOOKAD, THUKDANUY\n')
  outfile.write('SUKKEAW, PAWORNRAT\n')
  outfile.write('SUNUNTA, NEERANUCH\n')
  outfile.write('TIENKAEW, SUNISA\n')
  outfile.write('WIANGLO, DANAI\n')
  outfile.write('WONGRIAB, NOPPADOL\n')
  outfile.write('YAMMEE, CHAWAN')
  
  # Close the file
  outfile.close()
  
# Call the main function
if __name__ == '__main__':
      main()
