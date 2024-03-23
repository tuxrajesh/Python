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

listNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
listNode.print_list(listNode.remove_nth_from_end_optimal(listNode, 5))

# listNode = ListNode(1)
# listNode.print_list(listNode.remove_nth_from_end(listNode, 1))

# listNode = ListNode(1, ListNode(2))
# listNode.print_list(listNode.remove_nth_from_end(listNode, 1))