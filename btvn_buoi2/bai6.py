n = int(input("Nhap n: "))
print("So hoan hao tu 1 den ",n, "la: ")
for i in range(1, n + 1):
    sum = 0
    for j in range(1, i):
        if i % j ==0:
            sum += j
    if sum == i:
        print(i , end=' ')