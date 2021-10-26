data = []
count = 0
with open("reviews.txt", "r") as r:
	for line in r:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print("檔案讀完了, 總共有", len(data), "筆資料。")

sum_len = 0
for d in data:
	sum_len += len(d)
print("留言的平均長度是", sum_len/len(data))

print(data[1000000 - 1]) #這會印出清單中最後一筆留

print(d) #這也會印出清單中最後一筆留

