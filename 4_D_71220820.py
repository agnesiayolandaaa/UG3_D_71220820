nama = input("Masukkan Nama Lengkap Anda:")
prodi = input ("Masukkan Prodi Anda:")
try:
    nilai = input("Masukkan Nilai(dalam Huruf) yang anda Dapat:")

    if nilai == 'A' or 'a':
        print ('Nilai anda adalah 4.0, tbl tbl serem bgt lohh')
    elif nilai == 'A-' or 'a-':
        print ('Nilai anda adalah 3.75, kamu keren!')
    elif nilai == 'B+' or 'b+':
        print ('Nilai anda adalah 3.25 ')
    elif nilai == 'B' or 'b':
        print ('Nilai anda adalah 3.0 ')
    elif nilai == 'B-' or 'b-':
        print ('Nilai anda adalah 2.75, kurang semangat belajar nihh')
    elif nilai == 'C+' or 'c+':
        print ('Nilai anda adalah 2.25 ')
    elif nilai == 'C' or 'c':
        print ('Nilai anda adalah 2.0 ')
    elif nilai == 'D' or 'd':
        print ('Nilai anda adalah 1, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai == 'E' or 'e':
        print ('Nilai anda adalah 0, niat kuliah nggak sih???')
    else :
        print ('Inputan nilai yang anda masukkan tidak valid')
except :
    print ('Inputan nilai yang anda masukkan tidak valid')