# =====================================
# Tugas mandiri 1 - program percabangan
# Nama : Rahmatan Gani
# NIM  : 714260001
# kelompok : 6 THE CHANGCUTERS
# kelas : 1A

print("=" * 45)
print("KONVERSI NILAI ANGKA KE HURUF MUTU")
print("=" * 45)

try:
    nilai = float(input("Masukkan nilai (0 sampai 100): "))
except ValueError:
    print("\n[ERROR] Input harus berupa angka, contoh: 85 atau 85.5")
    print("=" * 45)
    exit()

if nilai < 0 or nilai > 100:
    print("\n[ERROR] Nilai harus berada dalam rentang 0 - 100!")
    print("=" * 45)
else:
    if nilai >= 90:
        huruf, keterangan = "A", "Lulus"
    elif nilai >= 80:
        huruf, keterangan = "B", "Lulus"
    elif nilai >= 70:
        huruf, keterangan = "C", "Lulus"
    elif nilai >= 50:
        huruf, keterangan = "D", "Tidak Lulus"
    elif nilai >= 20:
        huruf, keterangan = "E", "Tidak Lulus"
    else:
        huruf, keterangan = "F", "Tidak Lulus"

    print("\n" + "=" * 45)
    print("HASIL KONVERSI")
    print("=" * 45)
    print(f"Nilai Angka : {nilai:g}")
    print(f"Huruf Mutu  : {huruf}")
    print(f"Keterangan  : {keterangan}")
    print("=" * 45)
    print("Terima kasih telah menggunakan program ini!")
    print("=" * 45)
