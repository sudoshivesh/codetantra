#Write a program to print the number of lines, words, and characters in a file.
#Note: Let us consider the input file as 'InputData2.txt'.
#Given Filename is InputData2.txt

fin = open('InputData2.txt' , 'r')
charCount = wordCount = lineCount = 0
for line in fin:
  
  line.strip("\n")
  words=line.split()
  
  lineCount+=1
  wordCount+=len(words)
  charCount+=len(line)
  
fin.close()
print("Line count = ",lineCount)
print("Word count = ",wordCount)
print("Char count = ",charCount)
