class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.temp = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.temp = new_node
        else:
            self.temp.next = new_node
            new_node.prev = self.temp
            self.temp = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.append(data)
            return
        temp = self.head
        new_node.next = temp
        temp.prev = new_node
        self.head = new_node

    def print_list(self):
        curr = self.head
        if curr is None:
            return "Doubly Ll is empty"
        while curr:
            print(curr.data)
            curr = curr.next

    def add_after(self, data, key):
        new_node = Node(data)
        curr = self.head
        while curr:
            if curr.next is None and curr.data == key:
                self.append(data)
                return
            elif curr.data == key:
                new_node.prev = curr
                new_node.next = curr.next
                curr.next.prev = new_node
                curr.next = new_node
                return
            curr = curr.next
        return "Key no present"

    def add_before(self, data, key):
        new_node = Node(data)
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
                self.prepend(data)
                return
            elif curr.data == key:
                new_node.prev = curr.prev
                new_node.next = curr
                curr.prev.next = new_node
                curr.prev = new_node
                return
            curr = curr.next
        return "no key like dis here bitch"


ls1 = DoublyLL()
ls1.append(2)
ls1.append(3)
ls1.append(4)
ls1.prepend(1)
ls1.add_after(data=11, key=1)
ls1.add_after(data=12, key=2)
ls1.add_before(data=10, key=1)
ls1.print_list()
# print(ls1.head.prev)
