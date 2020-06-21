# -*- coding: utf-8 -*-

import mouse

'''
官方文件
https://github.com/boppreh/mouse
'''

# 左鍵一下
mouse.click(button='left')

# 右鍵兩下
mouse.double_click(button='right')

# 向上滾動
mouse.wheel(delta=10)

# 向下滾動
mouse.wheel(delta=-10)

# 得到當前座標 (x, y)
(x, y) = mouse.get_position()

# 移動至絕對座標
mouse.move(x=100, y=200)

# 從絕對座標 (start_x, start_y) 拖曳至 (end_x, end_y)
mouse.drag(start_x=100, start_y=100, end_x=500, end_y=600, duration=5)

# 移動至相對位置
mouse.move(x=100, y=200, absolute=False)

# 從相對位置 (start_x, start_y) 拖曳至 (end_x, end_y)
mouse.drag(start_x=100, start_y=100, end_x=500, end_y=600, absolute=False, duration=5)