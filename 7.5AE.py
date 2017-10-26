phonenumold = int(input("Enter a 10-character telephone number: \n "))
print(phonenumold)

split = phonenumold.split('-')
print(split)

last4 = split[2]

last_num = 0

while last_num <4:
    if last4[last_num] is 'A' or "B" or 'C':
        print('2')
    if last4[last_num] is 'D' or "E" or 'F':
        print('3')
    if last4[last_num] is 'G' or "H" or 'I':
        print('4')
    if last4[last_num] is 'J' or "K" or 'L':
        print('5')
    if last4[last_num] is 'M' or "N" or 'O':
        print('6')
    if last4[last_num] is 'P' or "Q" or 'R' or 'S':
        print('7')
    if last4[last_num] is 'T' or "U" or 'V':
        print('8')
    if last4[last_num] is 'W' or "X" or 'Y' or 'Z':
        print('9')
    last_num += 1