#https://www.w3resource.com/python-exercises/python-basic-exercises.php

#1. Write a Python program to print the following string in a specific format 
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up 
#above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star,
#How I wonder what you are" Output :

#Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How I wonder what you are


lullaby = "Twinkle, twinkle, little star, How I wonder what you are! Up\
above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star,\
How I wonder what you are"

lullaby_formated = "Twinkle, twinkle, little star," + "\n" +\
"\t" + "How I wonder what you are!" + "\n" +\
"\t" + "\t" + "\t" + "Up above the world so high," + "\n" +\
"\t" + "\t" + "\t" + "Like a diamond in the sky." + "\n" +\
"Twinkle, twinkle, little star," + "\n" +\
"\t" + "How I wonder what you are"

print(lullaby_formated)


