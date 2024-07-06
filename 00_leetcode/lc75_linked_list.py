from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 002095
        c = 0
        n = head
        while n:
            c += 1
            n = n.next
        # print("count: {}".format(c))
        if c == 1:
            return None
        m = c // 2 - 1
        n = head
        while m > 0:
            n = n.next
            m -= 1
        n.next = n.next.next
        return head


    def printList(self, head):
        s = ""
        while head:
            s = s + str(head.val) + " "
            head = head.next
        return s


    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 000328
        h, h_o, h_e, head_o, head_e, even = head, None, None, None, None, True
        if h:
            even = not even
            # print("val: {}, even: {}".format(h.val, even))
            h_o = h
            head_o = h_o
            h = h.next
        if h:
            even = not even
            # print("val: {}, even: {}".format(h.val, even))
            h_e = h
            head_e = h_e
            h = h.next
        while h:
            even = not even
            # print("val: {}, even: {}".format(h.val, even))
            if even:
                h_e.next = h
                h_e = h_e.next
            else:
                h_o.next = h
                h_o = h_o.next
            h = h.next
        if h_e:
            h_e.next = None
        if h_o:
            h_o.next = head_e
        # print("head_e: {}".format(self.printList(head_e)))
        # print("head_o: {}".format(self.printList(head_o)))
        # print("h_e: {}".format(self.printList(h_e)))
        # print("h_o: {}".format(self.printList(h_o)))
        return head_o


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 000206
        if head:
            last = self.reverseListHelp(head)
            head.next = None
            # while last:
            #     print("last: {}".format(last.val))
            #     last = last.next
            return last
        else:
            return head


    def reverseListHelp(self, n):
        # print("n.val: {}".format(n.val))
        if n.next:
            last = self.reverseListHelp(n.next)
            n.next.next = n
            return last
        else:
            return n


    def pairSum(self, head: Optional[ListNode]) -> int:
        # 002130
        n, c, s = head, 0, []
        while n:
            s.append(n.val)
            n = n.next
            c += 1
        half, s_max, i = c // 2, -sys.maxsize - 1, 0
        while i < half:
            s_max = max(s_max, s[i] + s[c-(i+1)])
            i += 1
        return s_max


if __name__ == '__main__':
    s = Solution()
