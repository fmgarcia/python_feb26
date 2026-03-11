class Sorting:
    
    def __init__(self, arr):
        self.arr = arr
    
    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr
    
    def selection_sort(self):
        n = len(self.arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
        return self.arr
    
    
    def insertion_sort(self):
        n = len(self.arr)
        for i in range(1, n):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr
    
    def merge_sort(self):
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            L = self.arr[:mid]
            R = self.arr[mid:]

            left_sorter = Sorting(L)
            right_sorter = Sorting(R)

            left_sorter.merge_sort()
            right_sorter.merge_sort()

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    self.arr[k] = L[i]
                    i += 1
                else:
                    self.arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                self.arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                self.arr[k] = R[j]
                j += 1
                k += 1
        
        return self.arr
    
    def quick_sort(self):
        if len(self.arr) <= 1:
            return self.arr
        else:
            pivot = self.arr[0]
            less_than_pivot = [x for x in self.arr[1:] if x < pivot]
            greater_than_pivot = [x for x in self.arr[1:] if x >= pivot]
            return Sorting(less_than_pivot).quick_sort() + [pivot] + Sorting(greater_than_pivot).quick_sort()
        
    def heap_sort(self):
        n = len(self.arr)

        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l

            if r < n and arr[r] > arr[largest]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(self.arr, n, i)

        for i in range(n-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            heapify(self.arr, i, 0)

        return self.arr
        
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorter = Sorting(arr)
    print("Original array:", arr)
    print("Sorted array (Bubble Sort):", sorter.bubble_sort())
    print("Sorted array (Selection Sort):", sorter.selection_sort())
    print("Sorted array (Insertion Sort):", sorter.insertion_sort())
    print("Sorted array (Merge Sort):", sorter.merge_sort())
    print("Sorted array (Quick Sort):", sorter.quick_sort())
    print("Sorted array (Heap Sort):", sorter.heap_sort())
    print("Utilizando funciones del lenguaje: ", sorted(arr))