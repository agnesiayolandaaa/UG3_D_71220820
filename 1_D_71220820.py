curah_hujan = float(input("Masukkan nilai curah hujan:"))
kondisi_hujan = "Cuaca terang/berawan" if curah_hujan == 0  else "Curah hujan ringan" if curah_hujan >= 0 and curah_hujan <= 20  else "Curah hujan sedang" if curah_hujan > 20 and curah_hujan <= 50 else "Curah hujan lebat"  if curah_hujan > 50 and curah_hujan <= 100 else "Curah hujan ekstrem" 
print(kondisi_hujan)