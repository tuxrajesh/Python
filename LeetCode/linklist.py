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
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        head1 = list1
        head2 = list2

        node1 = list1
        node2 = list2
        while node1 is not None and node2 is not None:
            print(f"node1: {node1.val}, node2: {node2.val}")           
            if node1.val <= node2.val:
                brk = node1.next
                node1.next = node2
                node1 = brk                
            else:
                brk = node2.next
                node2.next = node1
                node2 = brk
        if head1.val <= head2.val:
            return head1
        else:
            return head2

# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
list1 = ListNode(5)
list2 = ListNode(1, ListNode(2, ListNode(4)))
listMerge = ListNode()
listMerge.print_list(listMerge.merge_two_sorted_lists(list1, list2))