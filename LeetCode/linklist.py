class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next

    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
    def print_list(self, head):
        print("------------------ LIST --------------------------")
        i = 0
        while head:
            i += 1
            if i > 50:
                break
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
    
    def palindrome_linked_list(self, head):
        """
        Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
        """
        self.print_list(head)
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        for i in range(len(values)):
            if values[i] != values[len(values) - i - 1]:
                return False
        return True
    
    def linked_list_cycle(self, head):
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        """
        elements = []
        pos = 0
        while head is not None:
            if head in elements:
                return True
            elements.append(head)
            pos += 1
            head = head.next
        return False
# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
# list1 = ListNode(5)
# list2 = ListNode(1, ListNode(2, ListNode(4)))
# list1 = ListNode(-7)
# list2 = ListNode(-10, ListNode(-10, ListNode(-9, ListNode(-4, ListNode(1, ListNode(6, ListNode(6)))))))
# listMerge = ListNode()
# listMerge.print_list(listMerge.merge_two_sorted_lists(list1, list2))
# list1 = ListNode(1, ListNode(2))
# print(list1.palindrome_linked_list(list1))
# list2 = ListNode(1, ListNode(2, ListNode(1)))
# print(list2.palindrome_linked_list(list2))
node1 = ListNode(4)
node2 = ListNode(3, node1)
node3 = ListNode(2, node2)
node4 = ListNode(1, node3)
node1.next = node3
node1.print_list(node4)
print(node4.linked_list_cycle(node4))