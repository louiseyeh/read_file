data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 ==0:    #%求餘數 每讀取10000筆資料顯示進度
			print(len(data))
print('檔案讀取完了總共有', len(data), '筆資料')

sum_len = 0
for d in data: #每一筆資料為d
	sum_len = sum_len + len(d) #累積每一筆長度
print('留言的平均長度是', sum_len / len(data))
