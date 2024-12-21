
def bubble_sort(data):
    panjang = len(data)  
    for i in range(panjang): 
        for j in range(0, panjang - i - 1):  
            if data[j] > data[j + 1]:  
                data[j], data[j + 1] = data[j + 1], data[j]
    return data  

angka = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]

print("List Sebelum Disorting:", angka)

angka_urut = bubble_sort(angka)

print("List Yang Sudah Disorting:", angka_urut)