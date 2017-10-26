def stringOperations(string):
    if ',' in string:
        splitWords = string.split(',')
        print('First word:',splitWords[0].strip())
        print('Second word:',splitWords[1].strip())
        print('')
    else:
        print('Error: No comma in string.\n')
    return

        print('Error: No comma in string.\n')


while True:
    string = input('Enter input string:\n')
    if string =='q':
        break
    else:
        stringOperations(string)

