def stringOperations(string):
    if ',' in string:
        splitWords = string.split(',')
        print('First word:',splitWords[0].strip())
        print('Second word:',splitWords[1].strip())
        print('')
    else:
<<<<<<< HEAD
    	print('Error: No comma in string.\n')
    return
=======
        print('Error: No comma in string.\n')
>>>>>>> 0991df25c8ace51da4289cf8372e63f30aaec362

while True:
    string = input('Enter input string:\n')
    if string =='q':
        break
    else:
        stringOperations(string)

