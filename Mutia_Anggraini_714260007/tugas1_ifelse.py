# ============================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : Mutia Anggraini
# NIM   : 714260007
# Kelas : 11
# ============================================================

print("=" * 45)
print("      PROGRAM KONVERSI NILAI MAHASISWA")
print("=" * 45)

# Meminta input nilai dari pengguna
try:
    nilai = float(input("Masukkan nilai akhir (0-100): "))

    print("-" * 45)

    if nilai < 0 or nilai > 100:
        print("Error: Nilai harus berada di rentang 0-100!")

    elif nilai >= 80:
        huruf = "A"
        keterangan = "Lulus"

    elif nilai >= 70:
        huruf = "B"
        keterangan = "Lulus"

    elif nilai >= 60:
        huruf = "C"
        keterangan = "Lulus"

    elif nilai >= 50:
        huruf = "D"
        keterangan = "Tidak Lulus"

    else:
        huruf = "E"
        keterangan = "Tidak Lulus"

    if 0 <= nilai <= 100:
        print(f"Nilai Angka   : {nilai:g}")
        print(f"Huruf Mutu    : {huruf}")
        print(f"Keterangan    : {keterangan}")

    print("=" * 45)
    print("Terima kasih telah menggunakan program ini!")

except ValueError:
    print("-" * 45)
    print("Error: Masukkan nilai berupa angka!")
    print("=" * 45)