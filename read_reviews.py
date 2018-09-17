data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 ==0:    #%求餘數 
			print(len(data))
print(len(data))
print(data[0])  #印出第一筆資料
print('----------')
print(data[1])  #印出第二筆資料
