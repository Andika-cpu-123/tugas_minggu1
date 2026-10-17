# =====================================
# Tugas mandiri 1 - program percabangan
# Nama : Rahmatan Gani
# NIM  : 714260001
# kelompok : 6 THE CHANGCUTERS
# kelas : 1A

print("=" * 45)
print("KONVERSI NILAI ANGKA KE HURUF MUTU")
print("=" * 45)

# Input dari user
nilai_input = input("Masukkan nilai akhir (0-100): ")

# Cek apakah input berupa angka
if not nilai_input.isdigit():
    print("\n[ERROR] Input harus berupa angka bulat!")
    print("=" * 45)
    exit()

nilai = int(nilai_input)

# Cek rentang nilai
if nilai < 0 or nilai > 100:
    print("\n[ERROR] Nilai harus berada dalam rentang 0 - 100!")
    print("=" * 45)
else:
    # Konversi ke huruf mutu (minimal 4 elif)
    if nilai >= 90:
        huruf = "A"
        keterangan = "Lulus"
    elif nilai >= 80:
        huruf = "B"
        keterangan = "Lulus"
    elif nilai >= 70:
        huruf = "C"
        keterangan = "Tidak Lulus"
    elif nilai >= 50:
        huruf = "D"
        keterangan = "Tidak Lulus"
    elif nilai <= 50:
        huruf = "E"
        keterangan = "Tidak Lulus"
    else:
        huruf = "E"
        keterangan = "Tidak Lulus"

    # Output dengan f-string
    print("\n" + "=" * 45)
    print("HASIL KONVERSI")
    print("=" * 45)
    print(f"Nilai Angka : {nilai}")
    print(f"Huruf Mutu  : {huruf}")
    print(f"Keterangan  : {keterangan}")
    print("=" * 45)
    print("Terima kasih telah menggunakan program ini!")
    print("=" * 45)
