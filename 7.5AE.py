phonenumold = input("Enter a 10-character telephone number:\n")
print(phonenumold)

split = phonenumold.split('-')
print(split)

last4 = split[2]

last_num = 0
L = '-'
nn = ''
for let in last4:

    if let == 'A' or let == 'B' or let == 'C':
        new = '2'
    elif let == 'D' or let == 'E' or let == 'F':
        new = '3'
    elif let == 'G' or let == 'H' or let == 'I':
        new = '4'
    elif let == 'J' or let == 'K' or let == 'L':
        new = '5'
    elif let == 'M' or let == 'N' or let == 'O':
        new = '6'
    elif let == 'P' or let == 'Q' or let == 'R' or let == 'S':
        new = '7'
    elif let == 'T' or let == 'U' or let == 'V':
        new = '8'
    elif let == 'W' or let == 'X' or let == 'Y' or let == 'Z':
        new = '9'

    nn = nn + new

print(split[0] + L + split[1] + L + nn)







