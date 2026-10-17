# ==============================================
# Latihan 1 - Kalkulator Konsol Sederhana
# Pelatian Dasar Pemrograman MORRIS IF 2026
# ==============================================

print("======================================")
print("Kalkulator Konsol Sederhana")
print("======================================")
print("Operasi yang tersedia: +, -, *, /")
print("======================================")

# - Bagian Input -
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")

print("======================================")

# - Bagian Proses -
if operasi == "+":
    hasil = num1 + num2
elif operasi == "-":
    hasil = num1 - num2
elif operasi == "*":
    hasil = num1 * num2
elif operasi == "/":
    hasil = num1 / num2
else:
    print("Operasi tidak valid!")
    exit()

print("======================================")
print(f"Hasil: {hasil}")

print("======================================")
print("Terima kasih telah menggunakan kalkulator ini!")