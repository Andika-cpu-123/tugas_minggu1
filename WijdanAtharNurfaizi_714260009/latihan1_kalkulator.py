# ("=" *40)
# Latihan 1 - Kalkulator Konsol Sederhana
# Pelatihan Dasar Pemrograman MORRIS IF 26
# ("=" *40)

print("=" *40)
print("    KALKULATOR KONSOL SEDERHANA")
print("=" *40)
print("Oprasi tersedia: + - * /")
print("-" *40)

# --- Bagian masukan pengguna ---
angka1 = float(input("Masukkan bilangan pertama : "))
angka2 = float(input("Masukkan bilangan kedua   :"))
operator = input("Masukkan operator (+ - * /): ")

print("-" *40)

# --- Bagian proses ---
if operator == "+":
   hasil = angka1 + angka2
   print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
   hasil = angka1 - angka2
   print(f"Hasil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
   hasil = angka1 * angka2
   print(f"Hasil: {angka1} * {angka2} = {hasil:.2f}")

elif operator == "/":
   if angka2 == 0:
      print("Kesalahan: bilangan tidak dapat dibagi dengan nol.")
   else:
      hasil = angka1 / angka2
      print(f"Hasil {angka1} : {angka2} = {hasil:.2f}")

else:
     print(f"Operator '{operator}' tidak dikenali.")
     print("Gunakan salah satu dari: + - * /")

print("=" *40)
print("Terima kasih telah menggunakan kalkulator ini.")            
   