# # Các cách khởi tạo chuỗi

# # my_string = 'Hello'

# # my_string = "Hello"

# # my_string = '''Hello'''

# # Sử dụng 3 dấu nháy kép để kéo dài chuỗi thành nhiều dòng
# # my_string = '''Hello, welcome to
# # the world of Python '''

# # print(my_string)

# # print('\a'): phát ra một tiếng bíp
# # \b: xóa ký tự trước nó

# # s='ab\nc'
# # print(s)

# #chuỗi trần
# # SRC=r'D:\coding\tennis_annalysist'
# # print(SRC)

# # định dạng số nguyên
# s1='Hệ nhị phân của {0} được biẻu diễn là {0:b}', format(12)
# print(s1)

# #Định dạng số thực
# s2="Biểu diễn dưới dạng mũ: {0:e}", format(1566.345)
# print(s2)

# #làm tròn số
# s3="Một phần ba: {0:.3f}". format(1/3)
# print(s3)

# #Căn lề
# s4='|{:<10}|{:^10}|{:>10}|'.format('list', 'tuple','set')
# print(s4)

# s1="HIT"
# s2="PYTHON"

# #Nối chuỗi
# s=s1+s2
# print(s)

# #Nhân bản chuỗi
# s=s1*3
# print(s)

# s='HIT PYTHON'

# for i in s:
#     print(i, end=' ')
# print()
# for i in range(len(s)):
#     print(s[i],end=' ')

# print(s[0:-3:2])
# # s=input()

#Thay đổi chuỗi
# s='HIT Python'
# s='...'
# print(s)

#Xóa chuỗi
# s='HIT Python'
# s='...'
# del s
# print(s)
# s='HIT Python'

# #Một số phương thức xử lý chuỗi
# s= s .lower()
# print(s)
# s1='hit python'
# s2='hit python'
# print(s==s1)
# print(id(s))
# print(id(s1))
# print(id(s2))

# s=input()
# s1=s.split()
# num=len(s1)
# print(num)

# print(len(input().split()))

# DANH SÁCH (LIST)
# l=[1,2,[3,4,5],6]
# print(l[2][-1])
# l=[x for x in range (10)]
# print(l)

# l=[int(input()) for _ in range(10)]
# print(l)

l=[[1,2,3],[4,5,6]]
# l=[i for l in l for i in l]
# print(l)

# C1:
# l=[x for x in range(10) if x%2==0]
# print(l)

# C2:
l=[]
for x in range(10):
    if x%2==0:
        l.append(x)
print(l)

# l=[1,2,3,4,5]
# print(l[0:4])

# #sửa, chèn, xóa
# l[0:3]=['a','b','c']
# print(l)
# l[:0]=[7,8,9]
# l[0:3]=[]
# print(l)

# l1=l.copy()
# print(id(l))
# print(id(l1))

l=input()
l1=l.split()
l2=[int(num) for num in l1]
print(l2.sort())

n= int (input())

a=[int(input()) for _ in range(n)]
b=[int(input()) for _ in range(n)]
a.sort()
print(a)

b=b*2
b=b[::-1]
c=b+a
print(c)