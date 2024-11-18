import time


def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
           
            if arr[j] < arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort_desc(arr):
   
    if len(arr) <= 1:
        return arr
    
    
    pivot = arr[-1]
    
    
    greater_than_pivot = [x for x in arr[:-1] if x >= pivot]  
    less_than_pivot = [x for x in arr[:-1] if x < pivot]      
    
    
    return quick_sort_desc(greater_than_pivot) + [pivot] + quick_sort_desc(less_than_pivot)


A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]


start_time = time.time()
sorted_A_bubble = bubble_sort_desc(A.copy())
sorted_B_bubble = bubble_sort_desc(B.copy())
bubble_sort_time = time.time() - start_time


start_time = time.time()
sorted_A_quick = quick_sort_desc(A.copy())
sorted_B_quick = quick_sort_desc(B.copy())
quick_sort_time = time.time() - start_time


print("Hasil dengan Bubble Sort:")
print("Array A setelah diurutkan:", sorted_A_bubble)
print("Array B setelah diurutkan:", sorted_B_bubble)
print(f"Waktu komputasi Bubble Sort: {bubble_sort_time:.6f} detik\n")

print("Hasil dengan Quick Sort:")
print("Array A setelah diurutkan:", sorted_A_quick)
print("Array B setelah diurutkan:", sorted_B_quick)
print(f"Waktu komputasi Quick Sort: {quick_sort_time:.6f} detik\n")


if bubble_sort_time < quick_sort_time:
    print("Bubble Sort lebih efisien untuk kasus ini.")
else:
    print("Quick Sort lebih efisien untuk kasus ini.")


# hasil menunjukkan bahwa algoritma bubblesort lebih efektif dibanding dengan quicksort, terlebih kita hanya memiliki dataset yang kecil, sehingga bubble sort lebih efektif saat ini. dan juga dikarenakan pada program tersebut pada quick sort menggunakan elemen terakhir sebagai pivot sehingga pembagian yang dihasilkan tidak seimbang
# dan juga secara umum perbedaan waktu nya tidak terlalu mencolok karena pada kasus A dan B hanya memiliki sedikit dataset nya.