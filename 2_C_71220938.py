kecepatan = int(input("masukkan kecepatan tempuh:"))
waktu = int(input("masukkan waktu:"))
#rumus
jarak = kecepatan*waktu
bensin = (jarak//10)
biaya = 15000*bensin
print("teman anda mengisi bensin sebanyak",bensin,"liter")
print("biaya yang dikeluarkan untuk mengisi bensin adalah","Rp.",biaya)

