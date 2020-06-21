# -*- coding: utf-8 -*-




for i in range(5):
    print('i:', i)

for j in range(3, 10):
    print('j:', j)

for k in range(10, 3, -2):
    print('k:', k)
    

name_list = ['Luffy', 'Nami', 'Sanji']
name_num = len(name_list)

for i in range(name_num):
    print(name_list[i])

for name in name_list:
    print(name)


score_dict = {'Luffy': 90, 'Nami': 70, 'Sanji': 80}

for key_name in score_dict:
    print(key_name, score_dict[key_name])
    



