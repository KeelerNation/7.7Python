title = input('Enter a title for the date:\n')
print('You entered: %s\n' % title)

header1 = input('Enter the column 1 Header:\n')
print('You entered %s\n' % header1)

header2 = input('Enter the column 2 Header:\n')
print('You entered %s\n' % header2)


while True:
    data = input('Enter a data point (-1 to stop input:\n')
    if data == '-1':
        break
    data = data.split(',')
    chart = {}
    chart.update({data[0]: data[1]})
    print(chart)
