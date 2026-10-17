print("=" *40 )
print("     Program Kalkulator Sederhana   ")
print("=" *40 )

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
pilih_operasi_penjumlahan = input("Pilih operasi (+, -, *, /): ")

if pilih_operasi_penjumlahan == "+":
    hasil = float(a) + float(b)
    print(f"Hasil penjumlahan {a} + {b} = {hasil}")

elif pilih_operasi_penjumlahan  == "-":
    hasil = float(a) - float(b)
    print(f"Hasil pengurangan {a} - {b} = {hasil}")

elif pilih_operasi_penjumlahan == "*":
    hasil = float(a) * float(b)
    print(f"Hasil perkalian {a} * {b} = {hasil}")

elif pilih_operasi_penjumlahan == "/":
    if float(b) != 0:
        hasil = float(a) / float(b)
        print(f"Hasil pembagian {a} / {b} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan atau tidak valid.")

print("=" *57 )
print(" terima kasih sudah menggunakan kalkulator sederhana ini ")
print("=" *57 )
