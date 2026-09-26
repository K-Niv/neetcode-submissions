# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(s, e):
            if e - s + 1 <= 1:
                return
            
            pivot = pairs[e]
            left = s
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    left += 1
            
            pairs[left], pairs[e] = pairs[e], pairs[left]
            sort(s, left - 1)
            sort(left + 1, e)
        
        sort(0, len(pairs) - 1)
        return pairs