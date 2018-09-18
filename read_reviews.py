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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(d), '筆留言長度<100字母')
print(new[0].strip())
print('--------')
print(new[1])

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
good = [d for d in data if 'good' in d]

print('一共有', len(good), '筆留言提到good')
print('第6筆資料', good[5])

good = [1 for d in data if 'good' in d]
print(good)

bad = ['bad' in d for d in data] #無篩選 1000000 個 true/false
# bad = []
# for d in data:
#	bad.append('bad' in d)
print(bad)
