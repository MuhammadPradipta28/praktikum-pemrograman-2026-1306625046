# Modul [02] - Program Faktor Bilangan

**Nama:** Muhammad Pradipta Arya Mujahid 
**NIM:** 1306625046  
**Kelas:** Fisika C  

---

## 1. Problem Statement
> Mencari semua faktor dari sembarang bilangan.

## 2. Mathematical Equation
> $\text{n} \text{ mod} \text{ i} =0$

## 3. Algorithm
> Tuliskan langkah-langkah logika penyelesaian masalah secara sistematis sebelum diimplementasikan ke dalam kode Python (`main.py`).
> 1. Mulai
> 2. Print "Program Faktor Bilangan"
> 3. Print "Nama = Muhammad Pradipta Arya Mujahid"
> 4. Print "NIM = 1306625046"
> 5. Input n"masukkan sembarang bilangan"
> 6. Periksa n=0?
>    6.1 Jika Ya, Print "Selesai" kemudian program berhenti
>    6.2 Jika Tidak, lanjut ke langkah berikutnya
> 7. Buat list kosong untuk menyimpan faktor
> 8. Inisialisasi i=1
> 9. Periksa i<=sqrt(n)?
>    9.1 Jika Tidak, lanjut ke langkah 12
>   9.2 Jika Ya, lanjut ke langkah berikutnya
> 10. Periksa n mod i=0?
>   10.1 Jika Ya, n/2 dan i dimasukkan ke list faktor
>   10.2 Jika Tidak, lanjut ke langkah berikutnya
>   10.3 Jika i=n/i, masukkan satu kali agar tidak duplikat
> 11. Tambahkan i=i+1, lalu kembali ke langkah 9
> 12. Print list faktor bilangan
> 13. Kembali ke langkah 5 untuk memasukkan bilangan lain
> 14. Selesai   
