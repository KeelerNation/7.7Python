title = input('Enter a title for the data:\n')
print('You entered: %s\n' % title)

header1 = input('Enter the column 1 header:\n')
print('You entered: %s\n' % header1)

header2 = input('Enter the column 2 header:\n')
print('You entered: %s\n' % header2)








data = ''

chart = {}

name_list = []
num_list = []
while data!='-1':
    while True:
        data = input('Enter a data point (-1 to stop input):\n')
        tt = data.split(',')
        if (data == '-1'):
            break
        elif ',' not in data:
            print('Error: No comma in string.\n')

        elif len(data.split(','))> 2:
            print('Error: Too many commas in input.\n')

        elif (tt[1].isdigit()) == False:
            print('Error: Comma not followed by an integer.\n')
        else:
            number = int(tt[1])
            data2 = data.split(',')
            dataa = data2[0]
            datab = data2[1]
            datab = datab.replace(' ', '')
            chart.update({dataa: datab})
            name_list.append(dataa)
            num_list.append(datab)
            print('Data string:', dataa)
            print('Data integer: %s' % datab)
            print('')


print('{:>33}'.format(title))
print('{:<20} | {:>23}'.format(header1, header2))
print('-'*46)



num = 0
for name in name_list:
    print('{:<20} | {:>23}'.format(name_list[num], num_list[num]))
    num = num + 1

num23 = 0
for name21 in name_list:
   print(name_list[num23], data[num23]*'*')
   num23 += 1









