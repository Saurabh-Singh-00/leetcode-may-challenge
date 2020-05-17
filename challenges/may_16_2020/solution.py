class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        if head.next == None:
            return head
        odd, even = head, head.next
        temp = even
        i = 1
        # Space Complexity O(3) for storing 3 references
        # Time Complexity O(n)
        while odd.next and even.next:
            if i % 2 != 0:
                odd.next = even.next
                if odd.next:
                    odd = odd.next
                even.next = odd.next
            else:
                even.next = odd.next
                if even.next:
                    even = even.next
                odd.next = even.next
            i += 1
        odd.next = temp
        return head


s = Solution()
head = ListNode(2)
t = head
l = [1, 3, 5, 6, 4, 7]
for i in l:
    t.next = ListNode(i)
    t = t.next
res = s.oddEvenList(head)
while res:
    print(res.val)
    res = res.next
