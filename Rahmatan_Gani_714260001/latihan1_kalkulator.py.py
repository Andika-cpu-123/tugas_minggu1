print("=" * 50)
print("     Program Kalkulator Sederhana")
print("=" * 50)

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
operator = input("Pilih operasi (+, -, *, /): ")

if operator == "+":
    hasil = a + b
    print(f"Hasil penjumlahan {a} + {b} = {hasil}")

elif operator == "-":
    hasil = a - b
    print(f"Hasil pengurangan {a} - {b} = {hasil}")

elif operator == "*":
    hasil = a * b
    print(f"Hasil perkalian {a} * {b} = {hasil}")

elif operator == "/":
    if b != 0:
        hasil = a / b
        print(f"Hasil pembagian {a} / {b} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak valid.")

else:
    print(f"Error: Operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu: +, -, *, /")

print("=" * 50)
print("Terima kasih sudah menggunakan kalkulator ini!")
print("=" * 50)
