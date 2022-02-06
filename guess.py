# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話印出 " 終於猜對了"
# 猜錯的話要告訴他 比答案大/小

import random

start = input('請決定開始值: ')
start = int(start)
end = input('請決定結束值: ')
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請輸入數字')
    num = int(num)
    if num == r:
        print("猜中了",)
        print('這是你猜第', count, '次')
        break
    elif num > r:
        print('再小一點')
    elif num < r:
        print('再大一點')
    print('這是你猜第', count, '次')
    