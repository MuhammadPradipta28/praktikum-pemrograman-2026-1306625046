
print("Program Konversi Suhu")
print("Nama : Muhammad Pradipta Arya Mujahid")
print("NRM  : 1306625046")

SuhuAwal = float(input("- Suhu awal  = "))
SuhuAkhir = float(input("- Suhu akhir = "))
Selang = float(input("- Selang     = "))

print("\nTABEL KONVERSI")
print("-" * 55)
print(f"{'No.':<6}{'Celcius':<12}{'Reamur':<12}{'Fahrenheit':<12}")
print("-" * 55)

no = 1
for celcius in range(int(SuhuAwal), int(SuhuAkhir) + 1, int(Selang)):
    reamur = (4/5) * celcius
    fahrenheit = (9/5) * celcius + 32

    print(f"{no:<6}{celcius:<12}{reamur:<12.1f}{fahrenheit:<12.1f}")
    no += 1

print("-" * 55)