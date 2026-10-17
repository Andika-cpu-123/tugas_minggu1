print("=" *40)
print("     KALKULATOR KONSOL SEDERHANA")
print("=" *40)
print("Operasi tersedia: + - * /")
print("-" *40)

# --- Bagian masukan pengguna ---
angka1 = float(input("Masukan bilangan pertama : "))
angka2 = float(input("Masukan bilangan kedua   :"))
operator = input("Masukkan operator (+ - * /): ")

print("-" *40)

# --- Bagian proses ---
if operator == "+":
   hasil = angka1 + angka2
   print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
      hasil = angka1 - angka2
      print(f"Hasil: {angka1} - {angka2} - {hasil:.2f}")

elif operator == "*":
      hasil = angka1 * angka2
      print (f"Hasil: {angka1} * {angka2} = {hasil:.2f}")
                                             

elif operator == "/":
      if angka2 == 0:
         print("Kesalahan: bilangan tidak dapat dibagi dengan nol.")
      else:
         hasil = angka1 / angka2
         print(f"Hasil {angka1} : {angka2} = {hasil:.2f}")
               
else:
          print(f"operator '{operator}' tidak kenali.")
          print("Gunakan salah satu dari: + - * /")

print("=" *40)
print("Terimah kasih telah menggunakan kalkulator ini.")