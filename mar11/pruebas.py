from mysorted import MySorted


def es_anagrama_selection_sort(str1, str2):  
    return MySorted().selection_sort(list(str1)) == MySorted().selection_sort(list(str2))

print("Testing MySorted class...")
print(MySorted().bubble_sort(list("hola")))
print(MySorted().selection_sort([64, 34, 25, 12, 22, 11, 90]))
print(MySorted().insertion_sort([64, 34, 25, 12, 22, 11, 90]))

print("Testing es_anagrama_selection_sort function...")
print(es_anagrama_selection_sort("listen", "silent"))  # True
print(es_anagrama_selection_sort("hello", "world"))    # False
print(MySorted().selection_sort(list("listen"))==MySorted().insertion_sort(list("silent"))) # True
