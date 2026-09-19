# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        if not lists:
            return None

        return self.mergeKListsHelper(lists, 0, len(lists) - 1)

    def mergeKListsHelper(
        self,
        lists: List[Optional[ListNode]],
        s: int,
        e: int
    ) -> Optional[ListNode]:

        # One list remains
        if s == e:
            return lists[s]

        m = (s + e) // 2

        left = self.mergeKListsHelper(lists, s, m)
        right = self.mergeKListsHelper(lists, m + 1, e)

        return self.mergeLists(left, right)

    def mergeLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next

        