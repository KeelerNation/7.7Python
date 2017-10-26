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
        if ',' in data:
            data3 = data.split(',')
            datac = data3[0]
            datad = data3[1]
            datad = datad.replace(' ', '')

        if (data == '-1'):
            break
        elif ',' not in data:
            print('Error: No comma in string.\n')

        elif len(data.split(','))> 2:
            print('Error: Too many commas in input.\n')

        elif (datad.isdigit()) == False:
            print('Error: Comma not followed by an integer.\n')
        else:
            number = int(datad)
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
print('{:<19} | {:>22}'.format(header1, header2))
print('-'*44)



num = 0
for name in name_list:
    print('{:<20} | {:>23}'.format(name_list[num], num_list[num]))
    num = num + 1


counter = 0
for x in range(0,len(num_list)):
    y = int(num_list[x])
    for z in range(0, y):
        print(name_list[counter], y*'*')
    counter += 1









