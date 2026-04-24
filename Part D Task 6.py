class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Task 6 Functions
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # FIXED: returns FIRST middle (for even nodes)
    def find_middle(self):
        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # if even number of nodes, return previous (first middle)
        if fast is None and prev:
            return prev.data

        return slow.data if slow else None

    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# Testing
ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

print("Original List:")
ll.display()

print("Number of nodes:", ll.count_nodes())
print("Middle element:", ll.find_middle())

ll.reverse_list()
print("Reversed list:")
ll.display()