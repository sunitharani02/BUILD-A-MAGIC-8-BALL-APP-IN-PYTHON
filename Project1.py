#import modules
import sys
import random

#initial variables
#loop variable
#list of responses variable
questions = True
responses = ["IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT, YES",
             "OUTLOOK LOOKS GOOD", "MOST LIKELY", "IT IS DECIDELY SO",
             "WITHOUT A DOUBT", "YES, DEFENITELY"]

#while loop
while questions:

#write the code that will recieve the user input
	ques = input("Ask a question. (press ENTER to quit)")

#return the random response
	magic_response = responses[random.randint(0,7)]

#and quit the application
#if statement
	if ques == "":
    		sys.exit()
	else:
    		print(magic_response)
    
