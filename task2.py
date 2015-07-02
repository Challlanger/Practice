import random
n = int(input('Input a number: '))
s = 9
for i in range(1, n):
    i = random.random()
    s += i
    print i
print ('Average: %.4f' % (s/n))
