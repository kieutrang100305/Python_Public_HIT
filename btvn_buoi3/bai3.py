# Nhập chuỗi s1 và s2 từ bàn phím
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

# In ra đảo ngược của chuỗi s1
dao_nguocs1 = s1[::-1]
print("Đảo ngược của chuỗi s1:", dao_nguocs1)

# Nhập vào 2 số nguyên a và b
a = int(input("Nhập số nguyên a (1 <= a < b <= len(s2)): "))
b = int(input("Nhập số nguyên b: "))

# In ra chuỗi s2 sau khi đảo ngược từ vị trí a đến b
dao_nguocs2 = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
print("Chuỗi s2 sau khi đảo ngược từ vị trí a đến b:", dao_nguocs2)

# In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn
s3 = s1[::2]
print("Chuỗi s3 sau khi xóa các kí tự vị trí chẵn:", s3)

# Trả về chuỗi s4 là đan xen các kí tự của s1 và s2
s4 = ''.join([x + y for x, y in zip(s1, s2)])
print("Chuỗi s4 đan xen các kí tự của s1 và s2:", s4)

# Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
doi_cho_s1 = s2[:2] + s1[2:]
doi_cho_s2 = s1[:2] + s2[2:]
print("Kết quả sau khi đổi chỗ 2 ký tự đầu tiên:")
print("s1 =", doi_cho_s1)
print("s2 =",doi_cho_s2)