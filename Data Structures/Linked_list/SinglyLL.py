class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def print_list(self):
        cur_node = self.head
        if self.head is None:
            return "Linked list is empty"
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.temp = new_node
        else:
            self.temp.next = new_node
            self.temp = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, data,pos):
        new_node = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if prev:
            prev.next = cur_node.next
            cur_node = None
        else:
            return "The ", key, "doesnt exists"

    def length(self):
        temp = self.head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        return l

    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def swap_two_nodes(self,key1,key2):
        temp1 = self.head
        prev1 = None
        temp2 = self.head
        prev2 = None
        if key1 == key2:
            return "same keys "
        while temp1 and temp1.data != key1:
            prev1 = temp1
            temp1 = temp1.next
        while temp2 and temp2.data != key2:
            prev2 = temp2
            temp2 = temp2.next
        if (temp1 or temp2) is None:
            return "Key invalid"
        if prev1:
            prev1.next = temp2
        else:
            self.head = temp2

        if prev2:
            prev2.next = temp1
        else:
            self.head = temp1
        temp1.next, temp2.next = temp2.next, temp1.next

    def reverse(self):
        prev_node = None
        curr_node = self.head
        next_node = self.head
        while curr_node:
            next_node = next_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def merge_sorted(self, list_):
        p = self.head
        q = list_.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
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

        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

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

    def remove_duplicates_2(self):
        temp = self.head
        ls = []
        prev = None
        while temp:
            if temp.data in ls:
                prev.next = temp.next

            else:
                ls.append(temp.data)
                prev = temp

            temp = prev.next

    def remove_duplicates_3(self):
        dup_values = dict()
        cur = self.head
        prev = None
        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def nth_to_last_node(self, n):
        # Method 1
        temp = self.head
        length = self.length()
        while temp:
            if length == n:
                print(temp.data)
                return temp
            length -= 1
            temp = temp.next
        if temp is None:
            print("Element ",n,"doesnt exist")
            return
        # method 2
        # p = self.head
        # q = self.head
        # # length = self.length()
        # while n:
        #     q = q.next
        #     n -= 1
        # if q is None:
        #     print("element", n, "doesnt exist")
        # while q:
        #     q = q.next
        #     p = p .next
        #
        # print(p.data)
        # return p

    def count_occurrences_iterative(self, data):
        temp = self.head
        count = 0
        while temp:
            if temp.data == data:
                count += 1
            temp = temp.next
        if not count:
            return "The element doesnt exist"
        return count

    def count_occurrences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)

    def rotate(self, k):
        temp_1 = self.head
        if k == 1:
            self.reverse()
            return

        while temp_1 and k-1:
            temp_1 = temp_1.next
            k -= 1

        if temp_1 is None:
            return "element", k, "Doesnt exists"

        temp_2 = temp_1.next
        temp_3 = temp_1.next
        temp_1.next = None
        while temp_2.next:
            temp_2 = temp_2.next

        temp_2.next = self.head
        self.head = temp_3

    def ispalindrome(self):
        # Method 1
        # temp1 = self.head
        # self.reverse()
        # temp2 = self.head
        #
        # while temp1.data == temp2.data:
        #     temp1 = temp1.next
        #     temp2 = temp2.next
        #     if not temp1 and temp2:
        #         break
        #
        # # if not temp1 and temp2:
        # #     return True
        # # else:
        # #     return False
        # return True if not temp1 and temp2 else False

        # Method 2
        # s = ""
        # p = self.head
        # while p:
        #     s += p.data
        #     p = p.next
        # return s == s[::-1]
        # Method 3 using stack
        p = self.head
        stack = []
        while p:
            stack.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = stack.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def move_tail_to_head(self):
        p = self.head
        prev = None
        while p.next:
            prev = p
            p = p.next
        prev.next = None
        p.next = self.head
        self.head = p

    def sum_two_list(self, ll):
        p = self.head
        q = ll.head
        carry = 0
        sum_llist = linkedList()
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            # j = q.data if q else 0  # if q exists then q.data is assigned to j otherwise the latter
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            print("S:", s)
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        if carry == 1:
            tail = sum_llist.head
            while tail.next:
                tail = tail.next
            tail.data += 10
        sum_llist.print_list()


# ls1 = linkedList()
# ls1.append()
# ls2.append(2)
# ls2.append(2)
# ls2.append(2)