from database import *

while True:

    print("\n===== SISTEM PARKIR PINTAR =====")
    print("1. Tambah Kendaraan")
    print("2. Tampilkan Data")
    print("3. Cari Plat")
    print("4. Update Data")
    print("5. Hapus Data")
    print("6. Lihat Antrian")
    print("7. Sorting")
    print("8. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_data()

    elif pilih == "2":
        tampil_data()

    elif pilih == "3":
        cari_data()

    elif pilih == "4":
        update_data()

    elif pilih == "5":
        hapus_data()

    elif pilih == "6":
        tampil_antrian()

    elif pilih == "7":
        sorting_data()

    elif pilih == "8":
        print("Program selesai.")
        break

    else:
        print("Menu tidak tersedia.")