n, m = map(int, input("Nhập số lượng phần tử của mảng và các tập hợp A, B: ").split())

mang = list(map(int, input("Nhập các phần tử của mảng: ").split()))

tap_hop_A = set(map(int, input("Nhập các phần tử của tập hợp A: ").split()))

tap_hop_B = set(map(int, input("Nhập các phần tử của tập hợp B: ").split()))

muc_do_hanh_phuc = 0

for phan_tu in mang:
    if phan_tu in tap_hop_A:
        muc_do_hanh_phuc += 1
    elif phan_tu in tap_hop_B:
        muc_do_hanh_phuc -= 1

print("Tổng mức độ hạnh phúc của bạn là:", muc_do_hanh_phuc)
