def bubble_sort(data):
    panjang = len(data)  
    for i in range(panjang):  
        for j in range(0, panjang - i - 1):  
            if data[j] > data[j + 1]:  
                data[j], data[j + 1] = data[j + 1], data[j]
    return data  

def binary_search(data, target):
    kiri = 0  
    kanan = len(data) - 1  

    while kiri <= kanan:  
        tengah = (kiri + kanan) // 2  
        if data[tengah] == target:  
            return tengah  
        elif data[tengah] < target:  
            kiri = tengah + 1  
        else:  
            kanan = tengah - 1  

    return -1  

angka = [23, 2, 89, 31, 15, 56, 87, 3, 34, 78]
print("Daftar angka (acak):", angka)

target = int(input("Masukkan angka yang ingin dicari: "))

angka_urut = bubble_sort(angka)
print("Daftar angka setelah diurutkan:", angka_urut)

hasil = binary_search(angka_urut, target)

if hasil != -1:
    print(f"Angka {target} ditemukan di indeks {hasil}.")
else:
    print(f"Angka {target} tidak ditemukan.")