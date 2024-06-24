def quick_sort(array, low, high):
  if low < high:
    pivot = partition(array, low, high)
    quick_sort(array, low, pivot - 1)
    quick_sort(array, pivot + 1, high)

  return array

def partition(array, low, high):
  pivot = array[high].lower()
  i = low - 1

  for j in range(low, high):
    if array[j].lower() <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]

  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1

array = ["Budi", "Agus", "Caca", "Dody", "Edi"]
print("Array nama sebelum diurutkan:", array)

array = quick_sort(array, 0, len(array) - 1)
print("Array nama setelah diurutkan:", array)
