#Python Exploration
#CS344
#Edgar Perez

#TO RUN IT JUST DO: 'python mypython.py' (whitout the ' ')

#Modules
import random
import string
import os
import io

#function that generates random lowercase leters given a range
def random_char(y):
	return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

#create files if they dont exist
file1 = open("uno", "w+") #uno means one lol
file2 = open("dos", "w+") #dos means two
file3 = open("tres", "w+")#tres means three

#after creat the files write the random letters plus "\n" character at the end
# There is probaly a better way but this is what I did:
file1.write((random_char(10)) + "\n")
file2.write((random_char(10)) + "\n")
file3.write((random_char(10)) + "\n")
#close files after being read
file1.close()
file2.close()
file3.close()

# Read files created
file1 = open("uno", "r") #uno means one lol
file2 = open("dos", "r") #dos means two
file3 = open("tres", "r")#tres means three

#Display to stdout only 10 characters
print file1.read(10)
print file2.read(10)
print file3.read(10)
#close files after being read
file1.close()
file2.close()
file3.close()

# Generate first integer from 1 to 42
randomN1 = random.randint(1,42)
print randomN1

# Generate first integer from 1 to 42
randomN2 = random.randint(1,42)
print randomN2

# Display the result of (random number1 * random number2)
print (randomN1*randomN2)
