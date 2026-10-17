# =================================================
# Latihan 1 - Kalkulator Konsol Sederhana
# Pelatihan Dasar Pemograman MORRIS IF 26
# =================================================

print("===============================")
print("  KALKULATOR KONSOL SEDERHANA  ")
print("===============================")
print("Operasi tersedia: + _ * /")
print("-------------------------------")

# --- Bangian Masukan Pengguna ---
angka1 = float(input("Masukan Bilangan Pertama :"))
angka2 = float(input("Masukan Bilangan Kedua : "))
operator = input("masukan operator (+ - * /): ")

print("----------------------------------")

# --- Bagian Proses ---
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = { hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibari dengan nol.")

else:
    print(f"Operator '{operator}' tidak dikenali.")
    print(f"Gunakan salah satu dari: + - * /")

print("================================")
print("Terima Kasih Telah Menggunakan Kalkulator ini.")