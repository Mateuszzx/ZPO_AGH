from typing import List, Tuple


def quicksort(in_array: List[int]) -> List[int]:
    """Posortuj zakres tablicy metodą quicksort.

    :param in_array: tablica do posortowania
    :return: posortowana tablica
    """
    len_in_array = len(in_array)
    sorting_table = in_array[:]
    quick_help(in_array=sorting_table, start=0, end = len_in_array-1)

    return sorting_table


def quick_help(in_array: List[int], start: int, end: int):
    
    if end - start < 1:
        return in_array
    
    i = start
    j = end 
    pivot = in_array[int((i+j)/2)]

    while i <= j:
        while in_array[i] < pivot: 
            i += 1
        while in_array[j] > pivot:
            j -= 1

        if i <= j:
            in_array[i], in_array[j] = in_array[j], in_array[i]
            i += 1
            j -= 1

    if j > start:
        quick_help(in_array=in_array, start=start, end =j+1)
    if i < end:
        quick_help(in_array=in_array, start=i, end = end)

    
def bubblesort(in_array: List[int]) -> Tuple[List[int], int]:
    """Posortuj tablicę metodą bąbelkową.

    :param in_array: tablica do posortowania
    :return: krotka zawierająca posortowaną tablicę oraz liczbę wykonanych porównań
    """
    comparison = 0
    out_array  = in_array[:]
    len_array = len(out_array)
    swap = False

    for j in range(len_array - 1):
        swap = False
        for i in range(len_array-1 -j):
            comparison +=1
            if out_array[i] > out_array[i+1]:
                out_array[i], out_array[i+1] = out_array[i+1], out_array[i]          
                swap = True 
        if not swap:
            break
                
    return out_array, comparison
