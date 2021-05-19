class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
        self.temp = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.temp = new_node
        else:
            self.temp.next = new_node
            self.temp = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert_node(self,data,pos):
        new_node = Node(data)
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        # Node would be inserted at the designated position
        for i in range(pos-2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self,key):
        temp = self.head
        prev = None
        if temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def swap_nodes(self,key1, key2):
        temp1 = self.head
        prev1 = None

        while temp1 and temp1.data != key1:
            prev1 = temp1
            temp1 = temp1.next

        temp2 = self.head
        prev2 = None

        while temp2 and temp2.data != key2:
            prev2 = temp2
            temp2 = temp2.next

        if (temp1 or temp2) is None:
            return

        if prev1:
            prev1.next = temp2
        else:
            self.head = temp2

        if prev2:
            prev2.next = temp1
        else:
            self.head = temp1

        temp1.next, temp2.next = temp2.next, temp1.next

    def reverse_list(self):
        prev_node = None
        curr_node = next_node = self.head

        while curr_node:
            next_node = next_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def reverse_recursive(self):

        def reverse(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return reverse(cur,prev)

        self.head = reverse(cur=self.head, prev=None)

    def remove_duplicates(self):
        temp = self.head
        while temp is not None:
            # if temp.data not in ls:
            #     ls.append(temp.data)
            prev = temp
            temp1 = temp.next
            while temp1:
                # print("exectuijng?")
                # prev = temp
                # temp1 = temp.next
                if temp.data == temp1.data:
                    print("balkahka", temp1.data)
                    prev.next = temp1.next
                    temp1 = temp1.next
                    continue
                prev = temp1
                temp1 = temp1.next

            temp = temp.next

    def merge_list(self, ls1):
        p = self.head
        q = ls1.head
        s = None
        if p is None:
            return q
        if q is None:
            return p

        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if p is None:
            s.next = q
        if q is None:
            s.next = p
        return new_head


list1 = linked_list()
list2 = linked_list()
list1.append(1)
list1.append(5)
list1.append(7)
list1.append(9)

list2.append(2)
list2.append(3)
list2.append(4)
list2.append(6)
list2.append(8)
list2.append(10)

list1.merge_list(list2)
list1.print_list()








# A recursive function for merging of two linked list
# def merge_sorted(head1, head2):
#
#     temp = None
#     if head1 is None:
#         return head2
#     if head2 is None:
#         return head1
#
#     if head1.data <= head2.data:
#         temp = head1
#
#         temp.next = merge_sorted(head1.next, head2)
#     else:
#         temp = head2
#
#         temp.next = merge_sorted(head1, head2.next)