
string = str(input('Enter a sentence:\n')).split()
for word in string:
    print(word[1:] + word[0] + 'AY', end = " ")