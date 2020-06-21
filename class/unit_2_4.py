# -*- coding: utf-8 -*-


luffy_r = 90
luffy_s = 30
luffy_c = 20


''' Original '''

#luffy_avg =  (luffy_r+ luffy_s+ luffy_c)/3
#if luffy_avg >= 60 :
#    luffy_pass = True
#else:
#	luffy_pass = False
#
#print(luffy_avg, luffy_pass)


'''
With function
'''
def one_piece(run, science, cook):
    
    avg =  (run+science+cook)/3
    if avg >= 60:
        is_pass = True
    else:
        is_pass = False
    
    return avg, is_pass


#avg, is_pass = one_piece(90, 30, 20)
#print(avg, is_pass)
#
#avg, is_pass = one_piece(30, 90, 40)
#print(avg, is_pass)
#
#avg, is_pass = one_piece(20, 40, 90)
#print(avg, is_pass)

'''
With list dataset
'''

data_list = []
data_list.append({'name': 'Luffy', 'run': 90, 'science': 30, 'cook': 20})
data_list.append({'name': 'Nami', 'run': 30, 'science': 90, 'cook': 40})
data_list.append({'name': 'Sanji', 'run': 20, 'science': 40, 'cook': 90})

for data in data_list:
    avg, is_pass = one_piece(data['run'], data['science'], data['cook'])
    print(data['name'], avg, is_pass)

'''
With dict dataset
'''
data_dict = {}
data_dict['Luffy'] = {'run': 90, 'science': 30, 'cook': 20}
data_dict['Nami'] = {'run': 30, 'science': 90, 'cook': 40}
data_dict['Sanji'] = {'run': 20, 'science': 40, 'cook': 90}

for name in data_dict:
    print(name,data_dict[name]['run'])

for data in data_dict:
    avg, is_pass = one_piece(data_dict[name]['run'], data_dict[name]['science'], data_dict[name]['cook'])
    print(data['name'], avg, is_pass)
