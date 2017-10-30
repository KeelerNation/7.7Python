def vol(string):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'e', 'I', 'O', 'U']
    count = sum([1 for i in string if i in v])

    return count


#def con(string):


string = input('Enter a string:\n')
print(vol(string))