#class 59~60
#range範圍
#python 內建功能

import random
range(3) #[0,1,2,3,4]
range(5) #[0,1,2]


for i in range(3) :
	r = random.randint(0, 100)
	print('This is ', i +1, 'times : random number', r )

#更改開始值
#只能開始值開始 結束值不能meet
range(2,5) # [2, 3, 4 ]
range(8,14) # [8, 9, 10, 11, 12, 13 ]
range (10, 20 , 2) #[10, 12, 14, 16, 18] #遞增值 為2 不超過結尾值 # 階梯
range (10, 3. -2) # [10, 8, 6, 4] 遞減值 為2 不超過結尾值 # 階梯