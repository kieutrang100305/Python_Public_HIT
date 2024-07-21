# n = int(input("Nhap so nguyen duong: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
# print("Tong cac chu so la:", sum)

# n= int(input("Nhap so nguyen duong: "))
# sum=0
# for i in range (1, n+1):
#     if n%i==0:
#         sum+=i
# print("Tong cac chu so la uoc cua", n, "la: ", sum)

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if (a+b>c and a+c>b and b+c>a):
    CV = a+b+c
    if a == b == c:
        print("Day la tam giac deu")
    elif a == b or b == c or a == c:
        print("Day la tam giac can")
    else:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            print("Day la tam giac vuong")
        elif CV / 3 <= max(a, b, c) / 2:
            print("Day la tam giac tu")
        else:
            print("Day la tam giac nhon")
else:
    print("Day khong phai la tam giac")

