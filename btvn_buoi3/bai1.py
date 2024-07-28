n = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(n):
    lst.append(int(input()))
print("lst =",lst)

#Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list.
import math
x = int(input("Nhập x = "))
a = lst.count(x)
print("Số lần xuất hiện", x, "trong list là: ", a)

#Thay thế phần tử từ vị trí 2 -> 7 trong list thành [8, 5, 4, 0, 1, 3]
lst[2:8] =[8, 5, 4, 0, 1, 3]
print("List sau khi thay thế là: lst =", lst)

# #Tìm số lớn nhất, và nhỏ nhất trong list.
print("Số lớn nhất trong list là: ",max(lst))
print("Số nhỏ nhất trong list là: ",min(lst))

#Nhập một số Y tùy chọn từ bàn phím. Chèn số Y vào đầu list.
y = int(input("Nhập y = "))
lst.insert(0,y)
print("lst =",lst)

#kiểm tra các số trong list có sắp xếp theo thứ tự tăng dần hay giảm dần không. Nếu sắp xếp theo tăng dần thì in ra màn hình “TĂNG”, còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIÁM”, nếu không tăng không giảm thì in “NO”.
if lst.sort():
    print("TĂNG")
if lst.sort(reverse=True):
    print("GIẢM")
else:
    print("NO")

#Tạo một list mới có N phần tử. Các phần tử sẽ có vị trí từ 1 -> N. Với mỗi phần tử ở vị trí i (1 <= i <= N) giá trị của nó là tổng i phần tử đầu tiên của list cũ.
new_list = []
sum = 0

for i in range(n):
    sum += lst[i]
    new_list.append(sum)
print("Danh sách mới:", new_list)

#Tạo một list mới [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000] và sắp xếp nó theo thứ tự tăng dần của giá trị, và sắp xếp nó theo sự tăng dần của giá trị tuyệt đối.
lst2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
lst2.sort()
print("lst2 =", lst2)
for i in range(len(lst2)):
    lst2[i] = abs(lst2[i])
lst2.sort()
print("lst2 =", lst2)