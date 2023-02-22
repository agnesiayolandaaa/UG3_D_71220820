try:
    plat_nomor = int(input('Masukkan Plat Nomor : '))

    if plat_nomor >= 0 and plat_nomor <= 3000:
        print('Kendaraan Tersebut adalah Mobil')

    elif plat_nomor >= 3001 and plat_nomor <= 4000:
        print('Kendaraan Tersebut adalah Motor')

    elif plat_nomor >= 4001 and plat_nomor <= 5000:
        print('Kendaraan Tersebut adalah Angkutan Umum')

    else:
        print('Plat Nomor Tidak Terindikasi, harus terdapat nomor kendaraan setelah kode daerah')

except:
    print('Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan')