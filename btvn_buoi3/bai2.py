a = list(map(int, input("Nhập các phần tử của list a: ").split()))
k = len(a)
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

if n * m > k:
    print("NO")
else:
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        matrix.append(row)
    for row in matrix:
        print(row)