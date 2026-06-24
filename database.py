import csv
import os
from collections import deque

FILE = "parkir.csv"
antrian = deque()

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID","Plat","Jenis","JamMasuk","Status"])


def tambah_data():
    id = input("ID: ")
    plat = input("Plat Nomor: ")
    jenis = input("Jenis Kendaraan: ")
    jam = input("Jam Masuk: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, plat, jenis, jam, "Masuk"])

    antrian.append(plat)

    print("Data berhasil ditambah.")


def tampil_data():
    print("\n=== DATA PARKIR ===")

    with open(FILE, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)


def cari_data():
    plat = input("Masukkan plat: ")

    with open(FILE, "r") as f:
        reader = csv.reader(f)

        ditemukan = False

        for row in reader:
            if len(row) > 1 and row[1] == plat:
                print(row)
                ditemukan = True

        if not ditemukan:
            print("Data tidak ditemukan.")


def update_data():
    id_cari = input("ID yang diubah: ")

    data = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) > 0 and row[0] == id_cari:
                row[1] = input("Plat baru: ")
                row[2] = input("Jenis baru: ")
                row[3] = input("Jam baru: ")
                row[4] = input("Status: ")

            data.append(row)

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("Data berhasil diupdate.")


def hapus_data():
    id_hapus = input("ID yang dihapus: ")

    data = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if row[0] != id_hapus:
                data.append(row)

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("Data berhasil dihapus.")


def tampil_antrian():
    print("\n=== ANTRIAN ===")

    if len(antrian) == 0:
        print("Kosong")
    else:
        for i, kendaraan in enumerate(antrian, 1):
            print(i, kendaraan)


def sorting_data():
    with open(FILE, "r") as f:
        data = list(csv.reader(f))

    header = data[0]
    isi = data[1:]

    isi.sort(key=lambda x: x[1])

    print(header)

    for row in isi:
        print(row)