n = int(input("Nhap vao mot so n: "))
print("Cac cap so Amicable từ 1 đến", n, "là:")
for a in range(1, n + 1):
    sum_a = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i
    b = sum_a
    if b > a and b <= n:
        sum_b = 0
        for j in range(1, b):
            if b % j == 0:
                sum_b += j
        if sum_b == a:
            print(a, b)