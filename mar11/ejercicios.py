from ordenacion import Sorting

def is_anagram(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Sort the characters of both words and compare
    return sorted(word1) == sorted(word2)

def is_anagram_selection(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    word1_sorted = Sorting(list(word1))
    word1_sorted.selection_sort()
    word2_sorted = Sorting(list(word2))
    word2_sorted.selection_sort()
    return word1_sorted.arr == word2_sorted.arr

def is_anagram_insertion(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    word1_sorted = Sorting(list(word1))
    word1_sorted.insertion_sort()
    word2_sorted = Sorting(list(word2))
    word2_sorted.insertion_sort()
    return word1_sorted.arr == word2_sorted.arr


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))    # False
    print(is_anagram_selection("listen", "silent"))  # True
    print(is_anagram_selection("hello", "world"))    # False
    print(is_anagram_insertion("listen", "silent"))  # True
    print(is_anagram_insertion("hello", "world"))    # False