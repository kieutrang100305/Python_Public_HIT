n= int(input("Nhap so nguyen duong: "))
sum=0
for i in range (1, n+1):
    if n%i==0:
        sum+=i
print("Tong cac chu so la uoc cua", n, "la: ", sum)