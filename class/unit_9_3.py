# -*- coding: utf-8 -*-

import datetime

# 輸出當下時間
now = datetime.datetime.now()
print(now)

# 印出想要的內容
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# datetime 格式可以相減
diff = datetime.datetime.now() - now
diff_sec = diff.total_seconds()

# 將 datetime 轉成字串
now_str = now.strftime('%Y-%m-%d-%H-%M-%S')

