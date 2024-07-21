# n=int(input("n="))
# sum=0
# for i in range (1, n+1):
#         if i % 2 == 1:
#             sum += i
#         else:
#             sum -= i
# print("S(n)= ", sum)

n=int(input("n= "))
sum=0
for i in range (1,n+1):
    sum+=1/(i+1)
print("S(n)= ", sum)

# import math
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a == 0:
#     if b == 0:
#         print("Phuong trinh vo nghiem")
#     else:
#         print("Phuong trinh co nghiem duy nhat x =", -b/c)
# else:
#     dt = b * b - 4 * a * c
#     if dt == 0:
#         print("Phuong trinh co nghiem duy nhat x =", -b/(2 * a))
#     elif dt > 0:
#         x1 = (float)(-b + math.sqrt(dt))/(2 * a)
#         x2 = (float)(- b - math.sqrt(dt))/(2 * a)
#         print("Phuong trinh co 2 nghiem phan biet", "x1 =", x1, "x2 =", x2)
#     else:
#         print("Phuong trinh vo nghiem")

