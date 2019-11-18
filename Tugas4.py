daftar_nilai = []

ulangi = True
while ulangi :
    nama = input('Masukan Nama : ')
    nim = input('Masukan Nim : ')
    tugas = int(input('Masukan Nilai Tugas : '))
    uts = int(input('Masukan Nilai UTS : '))
    uas = int(input('Masukan Nilai UAS: '))
    akhir = (tugas * 30/100)+(uts * 35/100)+(uas * 35/100)

    daftar_nilai.append([nama, int(nim), int(tugas), int(uts), int(uas),int(akhir)])
    if  (input('Tambah data lagi (y/t)?') == 't'):
        ulangi = False

print('\nDaftar Nilai Mahasiswa:')
print("====================================================================")
print("|No. |      Nama      |    NIM     | Tugas |  UTS  |  UAS  | Akhir |")
print("====================================================================")
i = 0
for item in daftar_nilai:
    i += 1
    print("| {no:2d} | {nama:14s} | {nim:10d} | {tugas:5d} | {uts:5d} | {uas:5d} | {akhir:5.2f} |"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
print("====================================================================")
