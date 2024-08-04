# # Khai báo tuple
t0 = tuple ()

t1 = ()

t2 = ("Hello", 1, 2, ["some text", 1, 2])

t3 = "Hello", 1, 2, ["some text", 1, 2]

# print(f"t0={t0}\t(typle(t0)")
# print(f"t1={t1}\t(typle(t1)")
# print(f"t2={t2}\t(typle(t2)")
# print(f"t3={t3}\t(typle(t3)")

# print("t2[1]=", t2[1])
# print("t2[3][2]=", t2[3][2])

# t2=list(t2)
# t2[0]="HI"
# t2=tuple(t2)
# print(t2)

# s={1,2,1,2,3,6,4,5}
# print(s)
# s.add(10)
# print(s)

# s.update([11,12,13])
# print(s)

# s.remove(10)
# print(s)
# print(s.pop())
# print(s)

# s.discard(4)
# print(s)

# s1={1,2,3,4,5}
# print(s1)
# print(s1.issubset(s))
# print(s.issubset(s1))
# s={'blue', 'green', 'red'}
# s1={'yellow', 'red', 'orange'}
# print(s|s1)
# print(s&s1)
# # print(s-s1)
# # print(s^s1)

# #
# string="Hoc lap trinh Python cung HIT"
# # ("H", "o", "c", ..., "T")
# #Đếm số lượng phần tử chữ o xuất hiện

# # s="Hoc lap trinh Python cung HIT"
# # s1=s.split()
# # print(s1)
# #C1:
# result=[]
# for char in string:
#     if char==" ":
#         continue
#     result.append(char)
# print(tuple(result))

# #C2
# result2=[]
# for index in range(len(string)):
#     if string[index]==" ":
#         continue
#     result2.append(string[index])
# print("tuple2=",tuple(result2))

# #Cách 3: list comprehension
# result3=[char for char in string if char is not " " ]
# print("Tuple3=", tuple(result3))

# count=0
# occurences_char_o=[char for char in result if char == "o"]
# print("o occurences=", len(occurences_char_o))

# s={1,5,4,6,7,2}
# print(s)
# s.update([355,3,20,15])
# print(s)

#Cho 1 danh sách 
#In ra phần tử lớn thứ 2 trong danh sách

s1={1,1,2,2,3,3,4,4,5,5}
s=set(s)
l= list(s)
print(l[-2])