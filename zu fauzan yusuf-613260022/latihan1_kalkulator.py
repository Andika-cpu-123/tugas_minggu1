print("=" *40)
print("KALKULATOR KONSOL SEDERHANA")
print("=" *40)
print("Operasi tersedia:+-*/")
print("=" *40)

angka1 = float(input("masukkan bilangan pertama: "))
angka2 = float(input("masukan bilangan kedua: "))
operator = input("masukan operator(=-*/):")

print("=" *40)

if operator=="+":
    hasil=angka1+angka2
    print(f"hasil:{angka1}+{angka2}={hasil:.2f}")

elif operator=="-":
    hasil=angka1-angka2
    print(f"hasil:{angka1}-{angka2}={hasil:.2f}")

elif operator=="/":
    if angka2==0:
        print("kesalahan:bilangan tidak dapat dibagi dengan nol.")
    else:
        hasil=angka1/angka2
        print(f"hasil:{angka1}/{angka2}={hasil:.2f}")
else:
    print(f"operator'{operator}'tidak dikenali.")
    print("gunakan salah satu dari:=-*/")

print("=" *40)
print("terima kasih telah menggunakan kalkulator ini.")