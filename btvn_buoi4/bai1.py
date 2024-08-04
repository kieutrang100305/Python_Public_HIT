t = ("0","1","2","3","4","5","6","8","9")
t1 = tuple(int(x) for x in t)

sum  = 0
for num in t1:
    sum += num

avg = sum/ len(t1)

print("Tuple sau khi chuyển đổi:",t1)
print("Trung bình cộng các phần tử:",avg)