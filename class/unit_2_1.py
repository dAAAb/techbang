# -*- coding: utf-8 -*-

a = 1
b = 2.0

c_1 = 'This is string'
c_2 = 'This is ' + str(a)
c_3 = f'This is {a}'

d_1 = [1, 2, 3]
d_2 = [4]
d_2.append(5)
d_2.append(6)

e_1 = {}
e_1['name'] = 'Jarvus'
e_1['score'] = 100
e_2 = {'name': 'Jarvus', 'score': 100}

print(a)
print(a, b)
print('String:', c_2)

print(d_1)
print(d_1[0])
print(d_1[-1])
print(d_1[0:2])

print(e_1)
print(e_1['name'])

