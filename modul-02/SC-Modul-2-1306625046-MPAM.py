
import math

print("Program Faktor Bilangan")
print("Nama : Muhammad Radipa Arya Mujahid")
print("NIM  : 2306625046")

while True:
    n = int(input("\nMasukkan sembarang bilangan (0 untuk selesai): "))

    if n == 0:
        print("Selesai")
        break

    faktor = []
    i = 1

    while i <= math.sqrt(n):
        if n % i == 0:
            faktor.append(i)

            if i != n // i:
                faktor.append(n // i)

        i = i + 1

    faktor.sort()

    print("Faktor bilangan", n, "adalah:", faktor)