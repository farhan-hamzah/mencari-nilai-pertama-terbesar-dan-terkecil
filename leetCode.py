nums = list(map(int, input("Masukkan array: ").split()))
n = [0]
terbesar = nums[0]
terkecil = nums[0]

for i in range(len(nums)):
    if nums[i] > terbesar:
        terbesar = nums[i]
    if nums[i] < terkecil: 
        terkecil = nums[i]
hasil = n + [terbesar] + [terkecil]
print("Hasil:", hasil)
