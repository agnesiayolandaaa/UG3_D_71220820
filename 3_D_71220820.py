start = int(input("Masukkan awal deret: "))
end = int(input("Masukkan akhir deret: "))

for i in range(start, end+1):
    print(i, end=", ") if i % 6 != 0 and i % 8 != 0 else ""
