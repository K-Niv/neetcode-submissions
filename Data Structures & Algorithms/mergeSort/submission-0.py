# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)


    def mergeSortHelper(self, pairs: List[Pair], s:int, e:int) -> List[Pair]:

        if e - s + 1 <= 1:
            return pairs

        m = (s + e) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, arr: List[Pair], s:int, m: int, e: int) -> None:
        left = arr[s: m + 1]
        right = arr[m + 1: e + 1]

        i = 0
        j = 0
        k = s

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
