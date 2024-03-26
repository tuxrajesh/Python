class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next

    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
    def print_list(self, head):
        print("------------------ LIST --------------------------")
        while head:
            print(f"{head.val}", end=" -> ")
            head = head.next
        print("None")

    def remove_nth_from_end(self, head, n):
        self.print_list(head)
        if head is None:
            return None
        
        cnt = 0
        curr = head
        
        while curr is not None:
            cnt += 1
            curr = curr.next
            
        # if n = cnt; delete head
        if cnt == n:
            first = head.next
            head = None
            return first
        
        # position to remove
        pos = cnt - n
        curr = head
        while curr is not None:
            pos -= 1
            if pos == 0:
                break
            curr = curr.next
        
        node_to_remove = curr.next
        curr.next = curr.next.next
        node_to_remove = None
        return head
    
    def remove_nth_from_end_optimal(self, head, n):
        fastp = head
        slowp = head
        
        for i in range(n):
            fastp = fastp.next
        
        # n = total items in list
        if fastp is None:
            return head.next
        
        # move both pointers until fastp reaches end
        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next
        
        node_to_remove = slowp.next
        slowp.next = slowp.next.next
        node_to_remove = None
        return head
    
    def reverse_list(self, head):
        """reverse a linked list"""
        prev = None
        curr = head
        next = head.next
        
        while next is not None:            
            curr.next = prev
            prev = curr
            curr = next            
            next = next.next
        
        curr.next = prev
        prev = curr
        curr = next
                         
        return prev

    def merge_two_sorted_lists(self, list1, list2):
        """merge two sorted linked lists"""
        """example: 1 -> 2 -> 4, 1 -> 3 -> 4"""
        """output: 1 -> 1 -> 2 -> 3 -> 4 -> 4"""
        dummy = ListNode(0)
        curr = dummy
        while True:
            # if any list gets to the last; then attach tail to the remaining elements in the other list
            if list1 is None:
                curr.next = list2
                break
            if list2 is None:
                curr.next = list1
                break

            # compare the date of the list and whichever is smaller or equaal append to the last of the merged list and change the pointer to the next element
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            # move the tail
            curr = curr.next

        return dummy.next

# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
# list1 = ListNode(5)
# list2 = ListNode(1, ListNode(2, ListNode(4)))
list1 = ListNode(-7)
list2 = ListNode(-10, ListNode(-10, ListNode(-9, ListNode(-4, ListNode(1, ListNode(6, ListNode(6)))))))
listMerge = ListNode()
listMerge.print_list(listMerge.merge_two_sorted_lists(list1, list2))