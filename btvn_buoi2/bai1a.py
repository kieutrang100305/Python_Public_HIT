n = int(input("Nhap so nguyen duong: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print("Tong cac chu so la:", sum)