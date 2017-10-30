def vol(string):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'e', 'I', 'O', 'U']
    count = sum([1 for i in string if i in v])

    return count


def con(string):
    c = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
         'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H',
         'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')
    count = sum([1 for i in string if i in c])

    return count

string = input('Enter a string:\n')
print('Number of vowels:', vol(string))
print('Number of consonants:', con(string))