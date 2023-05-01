class Node:

    def __init__(self, data):
        self.data = data
        # pointers to the data chunks
        self.next = None 
        self.prev = None


class LinkedList:
     # I set the head node None as default, because when we initalize the class we don't have any contents yet
    def __init__(self):
        self.head = None

    def append(self, prop):
        # I get the last node and append a new node after it
        last_node = self.getTail()
        last_node.next = Node(prop)
        last_node.next.prev = last_node  # also set its previous node

    def insert(self, prop, index):
        # I find the "indexed" node and append after
        indexed_node = self.getIndexedNode(index)
        next_node = indexed_node.next
        indexed_node.prev = indexed_node
        indexed_node.next = Node(prop)
        indexed_node.next.next = next_node
        indexed_node.next.prev = indexed_node

    def delete(self, index):
        # I connect last and the next node together
        node = self.getIndexedNode(index)
        previous_node = self.getIndexedNode(index-1)
        previous_node.next = node.next

    def search(self, prop):
        i = 0
        node = self.head
        while node.next != None:
            if node.data == prop:
                break
            i += 1
            node = node.next
        print(i)

    def getIndexedNode(self, index):
        node = self.head
        i = 0
        while node.next != None and i < index:
            i += 1
            node = node.next
        return node

    def getTail(self):
        node = self.head
        while node.next != None:
            node = node.next 
        return node

    def visualise(self):
        values = []
        node = self.head
        while node.next != None:
            values.append(node.data)
            node = node.next
        values.append(node.data)

        print("HEAD " + " -> ".join([f"[{v}]" for v in values]) + ' TAIL')


linked_list = LinkedList()
linked_list.prev = None
linked_list.head = Node(1)
linked_list.append(2)
linked_list.append(3)
linked_list.visualise()

linked_list.insert(4, 0)
linked_list.insert(5, 1)
linked_list.visualise()

linked_list.search(2)

linked_list.delete(2)
linked_list.delete(2)
linked_list.delete(1)
linked_list.delete(2)
linked_list.delete(1)

linked_list.visualise()
