import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


def sortedInsert(head, data):
    current_head = head
    previous_head = head
    insert_in_last = True
    while current_head.next is not None:
        if current_head.data > data:
            inert_data = DoublyLinkedListNode(data)
            inert_data.next = current_head
            if previous_head != current_head:
                previous_head.next = inert_data
                inert_data.prev = previous_head
            else:
                current_head.prev = inert_data
                inert_data.prev = inert_data
                head = inert_data
            insert_in_last = False
            break
        else:
            previous_head = current_head
            current_head = current_head.next

    if insert_in_last:
        if current_head.data > data:
            inert_data = DoublyLinkedListNode(data)
            previous_head.next = inert_data
            inert_data.next = current_head
            inert_data.prev = previous_head
        else:
            inedata = DoublyLinkedListNode(data)
            current_head.next = inedata
            inedata.prev = current_head

    return head


t = int(input())

for t_itr in range(t):
    llist_count = int(input())

    llist = DoublyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    llist1 = sortedInsert(llist.head, data)

    print_doubly_linked_list(llist1, ' ')
