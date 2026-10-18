# ================================
# Tugas mandiri if else -  Program Percabangan
# Nama : Andika Dwi Permana
# NIM  : 714260002
# Kelompok : 6 The Changcuters
# Kelas : 1A
# ===============================

nilai = float(input("Masukkan nilai akhir (0-100): "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid! Masukkan nilai antara 0 sampai 100.")
else:
    if nilai >= 85:
        huruf = "A"
        keterangan = "LULUS"
    elif nilai >= 75:
        huruf = "B"
        keterangan = "LULUS"
    elif nilai >= 65:
        huruf = "C"
        keterangan = "LULUS"
    elif nilai >= 50:
        huruf = "D"
        keterangan = "TIDAK LULUS"
    elif nilai <= 50:
        huruf = "E"
        keterangan = "TIDAK LULUS"

    print(f"Nilai: {nilai}")
    print(f"Huruf mutu: {huruf}")
    print(f"Keterangan: {keterangan}")
