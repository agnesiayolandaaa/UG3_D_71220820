try:
    plat_nomor = int(input('Masukkan Plat Nomor : '))

    if plat_nomor >= 0 and plat_nomor <= 3000:
        print('Plat nomor diperuntukan untuk Mobil')

    elif plat_nomor >= 3001 and plat_nomor <= 4000:
        print('Plat nomor diperuntukan untuk Motor')

    elif plat_nomor >= 4001 and plat_nomor <= 5000:
        print('Plat nomor diperuntukan untuk angkutan umum')

    else:
        print('Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan')

except:
    print('Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan')