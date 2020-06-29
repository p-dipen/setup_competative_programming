import sys
import pathlib
outpath = str(pathlib.Path(__file__).parent.absolute())
inpath = str(pathlib.Path(__file__).parent.absolute())
outpath += '\output.txt'
inpath += '\input.txt'
sys.stdout = open(outpath, 'w')
sys.stdin = open(inpath, 'r')


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


def insertNodeAtPosition(head, data, position):
    pos = 0
    current_head = head
    previous_head = head
    while pos <= position:
        if pos == position:
            new_head = SinglyLinkedListNode(data)
            previous_head.next = new_head
            new_head.next = current_head
            return head
        else:
            pos += 1
            previous_head = current_head
            current_head = current_head.next
    return head


llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

data = int(input())

position = int(input())

llist_head = insertNodeAtPosition(llist.head, data, position)

print_singly_linked_list(llist_head, ' ')
