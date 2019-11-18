# Memasukkan data
n = 0                                                                           # Integer
nama = []                                                                       # Data yang ingin dimasukan
nim = []                                                                        # Data yang ingin dimasukan
tugas = []                                                                      # Data yang ingin dimasukan
uts = []                                                                        # Data yang ingin dimasukan
uas = []                                                                        # Data yang ingin dimasukan
akhir = []                                                                      # Data yang ingin dimasukan
mhsw = []                                                                       # Ini digunakan agar datanya rapih berurutan kebawah


# Looping
while True:                                                                     # statement while untuk status true
    s_nama = input("Nama :")                                                    # mengisi nama
    nama.append(s_nama)                                                         # menambahkan nama
    i_nim = int(input("NIM :"))                                                 # mengisi nim
    nim.append(i_nim)                                                           # menambahkan nim
    i_tugas = int(input("Nilai Tugas :"))                                       # mengisi nilai tugas
    tugas.append(i_tugas)                                                       # menambahkan nilai tugas
    i_uts = int(input("Nilai UTS :"))                                           # mengisi nilai uts
    uts.append(i_uts)                                                           # menambahkan nilai uts
    i_uas = int(input("Nilai UAS :"))                                           # mengisi nilai uas
    uas.append(i_uas)                                                           # menambahkan nilai uas
    i_akhir = (i_tugas * 30/100) + (i_uts * 35/100) + (i_uas * 35/100)          # penjumlahan nilai akhir
    akhir.append(i_akhir)                                                       # menambahkan nilai akhir
    jawab = input("Tambah data (y/t)?")                                         # decision untuk menambahkan data
    if jawab == 't':                                                            # statement false yang menutup while
        break                                                                   # untuk menutup statement
    n += 0                                                                      # ini proses looping
    mhsw.append(nama)                                                           # disini mhsw append digunakan untuk merapihkan output kebawah
    mhsw.append(nim)
    mhsw.append(tugas)
    mhsw.append(uts)
    mhsw.append(uas)
    mhsw.append(akhir)


# Cetak hasil                                                                   #segala macam output
print("===============================================================================")
print("No.  |       Nama       |   NIM   |   Tugas   |   UTS   |   UAS   |   Akhir   |")
print("===============================================================================")
for n in range(0, len(mhsw[n])):                                                #disertakan lend agar bisa pindah kebawah datanya
    print('|',n+1,'|       ',nama[n],'      |  ',nim[n],'  |  ',tugas[n],'  |  ',uts[n],'  |  ',uas[n],'  |  ',akhir[n],'  |') #rumusan untuk print data nya
print("===============================================================================")
