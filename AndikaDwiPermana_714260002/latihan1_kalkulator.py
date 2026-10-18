angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil:.2f}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} x {angka2} = {hasil:.2f}")
elif operator == "/":
    if angka2 == 0:
        print("Maaf, pembagian dengan nol tidak bisa dilakukan, coba masukkan pembagi selain 0 ya!")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil:.2f}")
else:
    print(f"Operator '{operator}' tidak dikenali! Gunakan +, -, *, atau /.")
