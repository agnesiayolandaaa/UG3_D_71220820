nama = input("Masukkan Nama Lengkap Anda:")
prodi = input ("Masukkan Prodi Anda:")
try:
    nilai = input("Masukkan Nilai(dalam Huruf) yang anda Dapat:")

    if nilai == 'A':
        print ('Nilai anda adalah 4.0, tbl tbl serem bgt lohh')
    elif nilai == 'A-':
        print ('Nilai anda adalah 3.75, kamu keren!')
    elif nilai == 'B+':
        print ('Nilai anda adalah 3.25 ')
    elif nilai == 'B':
        print ('Nilai anda adalah 3.0 ')
    elif nilai == 'B-':
        print ('Nilai anda adalah 2.75, kurang semangat belajar nihh')
    elif nilai == 'C+':
        print ('Nilai anda adalah 2.25 ')
    elif nilai == 'C':
        print ('Nilai anda adalah 2.0 ')
    elif nilai == 'D':
        print ('Nilai anda adalah 1, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai == 'E':
        print ('Nilai anda adalah 0, niat kuliah nggak sih???')
except nilai == 'F':
    print ('Inputan nilai yang anda masukkan tidak valid')