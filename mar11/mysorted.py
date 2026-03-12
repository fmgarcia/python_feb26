class MySorted:
    
    def bubble_sort(self, lst):
        n = len(lst)
        for i in range(n):
            for j in range(0, n-i-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst
    
    def selection_sort(self, lst):
        n = len(lst)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if lst[j] < lst[min_idx]:
                    min_idx = j
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
        return lst
    
    def insertion_sort(self, lst):
        n = len(lst)
        for i in range(1, n):
            key = lst[i]
            j = i - 1
            while j >= 0 and key < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
        return lst
    
    def merge_sort(self, lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            L = lst[:mid]
            R = lst[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i += 1
                else:
                    lst[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                lst[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                lst[k] = R[j]
                j += 1
                k += 1
        return lst      

    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[len(lst) // 2]
            left = [x for x in lst if x < pivot]
            middle = [x for x in lst if x == pivot]
            right = [x for x in lst if x > pivot]
            return self.quick_sort(left) + middle + self.quick_sort(right)
    
    def heap_sort(self, lst):
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

        n = len(lst)

        for i in range(n // 2 - 1, -1, -1):
            heapify(lst, n, i)

        for i in range(n-1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]
            heapify(lst, i, 0)
        
        return lst
    
      
if __name__ == "__main__":
    print(MySorted().bubble_sort(list("hola")))
    print(MySorted().selection_sort([64, 34, 25, 12, 22, 11, 90]))
    print(MySorted().insertion_sort([64, 34, 25, 12, 22, 11, 90]))
    print(MySorted().merge_sort(list("hola")))
    print(MySorted().quick_sort(list("hola")))
    print(MySorted().heap_sort([64, 34, 25, 12, 22, 11, 90]))
    