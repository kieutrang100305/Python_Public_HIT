n = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(n):
    lst.append(int(input()))
print("lst =",lst)

so_yeu_thich = {1, 3, 5, 7, 9}
a = []
for num in lst:
    if num % 10 in so_yeu_thich:
        a.append(num)

a.sort()
print("Số lượng số thầy Ba thích trong các số Nasus có là: ",len(a))
print("Các số thầy Ba thích theo thứ tự tăng dần mà Nasus có là: ",a)
