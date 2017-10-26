title = input('Enter a title for the date:\n')
print('You entered: %s\n' % title)

header1 = input('Enter the column 1 Header:\n')
print('You entered %s\n' % header1)

header2 = input('Enter the column 2 Header:\n')
print('You entered %s\n' % header2)








data = ''

chart = {}

name_list = []

while data!='-1':
    good_input = False
    while not good_input:
        data = input('Enter a data point (-1 to stop input:\n')
        if (data == '-1'):
            break
        elif ',' not in data:
            print('Error: No comma in string.')

        elif len(data.split(','))> 2:
            print('Too many commas in input.')

        else:
            data2 = data.split(',')
            dataa = data2[0]
            datab = data2[1]
            datab = datab.replace(' ', '')
            chart.update({dataa: datab})
            name_list.append(dataa)
            print('Data string:', dataa)
            print('Data integer:', datab)



for name in name_list:
    num = 0
    print(name, '|', chart[0])










