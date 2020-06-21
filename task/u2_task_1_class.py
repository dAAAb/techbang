# -*- coding: utf-8 -*-


'''
Sample
'''

print()
half_max = 10
for half_num in range(7):
    print( ' '*(half_max-half_num) + '*'*half_num +  '*'*(half_num-1) )
print( ' '*half_max + '▎')


'''
Task 1


              *
            *****
          ~~~~~~~~~
        *************
      ^^^^^^^^^^^^^^^^^
               ▎

star: *
tilde: ~
caret: ^

'''

tree = []
tree.append({'half_num': 1, 'symbol': 'star'})
tree.append({'half_num': 3, 'symbol': 'star'})
tree.append({'half_num': 5, 'symbol': 'tilde'})
tree.append({'half_num': 7, 'symbol': 'star'})
tree.append({'half_num': 9, 'symbol': 'caret'})

half_max = 15

print()
half_max = 17
for half_num in range(6):
    print( ' '*(half_max-half_num) + '*'*half_num +  '*'*(half_num-1) )
print( ' '*half_max + '▎')

