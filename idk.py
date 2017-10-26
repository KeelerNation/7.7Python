name = ['bob', 'Hi', 'bob']
num = [33, 44, 55]

for name in name:
    print(name, end=' ')
    for i in num:
        j = int(num[i])
        for j in range(0, 3):
            print('*', end='')