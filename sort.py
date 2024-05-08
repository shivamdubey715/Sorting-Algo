def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minI = i
        for j in range(i+1, n):
            if arr[j] < arr[minI]:
                minI = j
        arr[i], arr[minI] = arr[minI], arr[i]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1
        while j>-1 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
        
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i=j=k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i+=1
            else:
                arr[k] = right_half[j]
                j+=1
            k+=1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def partition(array, low, high):
    pivot = array[high]
 
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def get_array():
    return list(map(int, input("Enter space-separated integers for the array: ").split()))

def main():
    while True:
        arr = get_array()
        choice = input("Enter the choice\n")
        if choice == '1':
            bubble_sort = list(arr)
            bubbleSort(bubble_sort)
            print("Bubble Sorted Array:", bubble_sort)
        elif choice == '2':
            insertion_sort = list(arr)
            insertionSort(insertion_sort)
            print("Bubble Sorted Array:", insertion_sort)
        elif choice == '3':
            merge_sort = list(arr)
            mergeSort(merge_sort)
            print("Bubble Sorted Array:", merge_sort)
            
        elif choice == '4':
            selection_sort = list(arr)
            selectionSort(selection_sort)
            print("Bubble Sorted Array:", selection_sort)
            
        elif choice == '5':
            quick_sort = list(arr)
            quickSort(quick_sort, 0, len(arr)-1)
            print("Bubble Sorted Array:", quick_sort)
    
    
if __name__ == "__main__":
    main()
