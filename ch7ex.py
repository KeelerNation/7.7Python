string = input('Enter your full name:\n')

new = string.split(' ')
newstr1 = new[0]
newstr2 = new[1]
newstr3 = new[2]

print('%s. %s. %s.' % (newstr1[0:1], newstr2[0:1], newstr3[0:1]))