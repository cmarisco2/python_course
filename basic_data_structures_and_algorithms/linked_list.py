# build a basic singly linked list in python


class Node:
    def __init__(self, val=None, next=None) -> None:
        self._val = val
        self._next = next


class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self) -> str:
        tempPtr = self._head
        string = ""
        while tempPtr != None:
            string += f'{tempPtr._val} -> '
            tempPtr = tempPtr._next
        string += 'null'
        return string

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def add(self, item):
        """Adds item to the end with tail ptr ~ O(1) time"""
        if self.is_empty():
            self._head = Node(val=item)
            self._tail = self._head
        else:
            self._tail._next = Node(val=item)
            self._tail = self._tail._next
        self._size += 1

    def remove(self):
        """removes item from the beginning with head ptr ~ O(1) time"""
        if self.is_empty():
            return
        item = self._head._val
        if self.size() == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
        self._size -= 1
        return item


if __name__ == '__main__':
    my_list = LinkedList()
    print(my_list)
    print(f'is my_list empty? {my_list.is_empty()}')
    stuff = ['hello', 17, 22.49]
    print(f'adding the elements to my_list:{stuff}')
    for thing in stuff:
        my_list.add(thing)
    print(f'is my_list empty? {my_list.is_empty()}')
    print(f'my_list has a size of {my_list.size()}')
    print(f'my list: {my_list}')
    print(f'removing first item in my_list: {my_list.remove()}')
    print(f'my list afterwards: {my_list}')
    print(f'is my_list empty? {my_list.is_empty()}')
    print(f'my_list has a size of {my_list.size()}')
    print(f'emptying my list:')
    while my_list.size() > 0:
        my_list.remove()
    print(f'my list afterwards: {my_list}')
    print(f'is my_list empty? {my_list.is_empty()}')
    print(f'my_list has a size of {my_list.size()}')
