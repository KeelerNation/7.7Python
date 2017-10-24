import re

def stringOperations(choice):
    if re.search(',',choice):
        splitWords = choice.split(',')
        print()
        print("First word: ",splitWords[0].strip())
        print("Second word: ",splitWords[1].strip())
        print()
	else:
    	print('Error:No comma in string')

while True:
	print()
	choice = input('Enter input string:\n')
	if choice =='q':
    	break
    else:
        stringOperations(choice)
