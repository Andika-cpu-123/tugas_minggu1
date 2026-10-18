<<<<<<< HEAD
print("Hello, World!")  
=======
#menghitung Luas dan keliling persegi panjang
print("= Menghitung Luas Persegi Panjang =")

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas persegi panjang adalah: {luas}cm²")
print(f"Keliling persegi panjang adalah: {keliling}cm")

#menghitung jam, menit, dan detik dari total detik
total_detik = 3600

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{total_detik} detik = {jam} jam, {menit} menit, {detik} detik")

#perbandingan 
nilai = 10
print(nilai >= 5)  # True
print(nilai == 5)   # False
print(nilai <= 5)   # False
>>>>>>> 7415700 (Menyelesaikan PR Morris minggu pertama)
