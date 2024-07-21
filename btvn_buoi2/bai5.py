n= int(input("n= "))
print(f"Các số Armstrong bậc 3 từ 1 đến {n} là:")
for num in range(1, n + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    
    if num == sum:
        print(num)