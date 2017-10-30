phone_num_old = input("Enter a 10-character telephone number: \n ")

print(phone_num_old)

split = phone_num_old.split('-')
print(split)

last4 = list(split[2])
print(last4)

first_three = list(split[0])
print(first_three)

second_three = list(split[1])
print(second_three)


last_num = 0

while last_num <4:
    if last4[last_num] is 'A' or "B" or 'C':
        last4[last_num] = '2'
        break
    elif last4[last_num] is 'D' or "E" or 'F':
        last4[last_num] = '3'
        break
    elif last4[last_num] is 'G' or "H" or 'I':
         print('')
    elif last4[last_num] is 'J' or "K" or 'L':
        print('')
    elif last4[last_num] is 'M' or "N" or 'O':
        print('')
    elif last4[last_num] is 'P' or "Q" or 'R' or 'S':
        print('')
    elif last4[last_num] is 'T' or "U" or 'V':
        print('')
    elif last4[last_num] is 'W' or "X" or 'Y' or 'Z':
        print('')
    else:
        break
    last_num += 1
print(last4)
first_num = 0

while first_num < 3:
    if first_three[first_num] is 'A' or "B" or 'C':
        print('')
    if first_three[first_num] is 'D' or "E" or 'F':
        print('')
    if first_three[first_num] is 'G' or "H" or 'I':
        print('')
    if first_three[first_num] is 'J' or "K" or 'L':
        print('')
    if first_three[first_num] is 'M' or "N" or 'O':
        print('')
    if first_three[first_num] is 'P' or "Q" or 'R' or 'S':
        print('')
    if first_three[first_num] is 'T' or "U" or 'V':
        print('')
    if first_three[first_num] is 'W' or "X" or 'Y' or 'Z':
        print('')
    first_num += 1

print(first_three)
second_num = 0

while second_num < 3:
    if second_three[second_num] is 'A' or "B" or 'C':
        second_three[second_num] = '2'
        break
    elif second_three[second_num] is 'D' or "E" or 'F':
        second_three[second_num] = '3'
        break
    elif second_three[second_num] is 'G' or "H" or 'I':
        print('')
    elif second_three[second_num] is 'J' or "K" or 'L':
        print('')
    elif second_three[second_num] is 'M' or "N" or 'O':
        print('')
    elif second_three[second_num] is 'P' or "Q" or 'R' or 'S':
        print('')
    elif second_three[second_num] is 'T' or "U" or 'V':
        print('')
    elif second_three[second_num] is 'W' or "X" or 'Y' or 'Z':
        print('')

    continue
    second_num += 1

print(second_three)

''.join(first_three)
''.join(second_three)
''.join(last4)

new_phone_num = '-'.join(split)

print(new_phone_num)