class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next
        print(f"{self.val}, {self.next}")

    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def remove_nth_from_end(self, head, n):
        node_cnt = 1
        
        node = head
        while node.next != None:
            print(f"Node: {node_cnt}\t Value: {node.val}\t Next: {node.next}")
            node = node.next            
            node_cnt += 1        
        
        node = head
        for i in range(1, node_cnt - n + 1):
            print(f"Node: {i}: Val: {node.val}")
            node = node.next
        
        for i in range(n, node_cnt):
            node.val = node.next.val
            node.next = node.next.next
        
        return head

listNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(listNode)
print(listNode.remove_nth_from_end(listNode, 2))