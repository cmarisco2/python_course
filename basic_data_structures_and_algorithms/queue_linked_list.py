
from linked_list import LinkedList


class Queue:

    def __init__(self) -> None:
        self._q = LinkedList()

    def __repr__(self) -> str:
        return str(self._q)

    def is_empty(self):
        return self._q.is_empty()

    def size(self):
        return self._q.size()

    def enqueue(self, object):
        self._q.add(object)

    def dequeue(self):
        return self._q.remove()


if __name__ == '__main__':

    my_queue = Queue()
    print(my_queue)
    obj = ['hi', 'bye', 21, 'yolo', True, 16.345]
    print(f'Enqueue objecst: {obj}')
    for thing in obj:
        my_queue.enqueue(thing)
    print(f'my queue is:\n{my_queue}')
    print(f'dequeue 2 objects')
    for num in range(2):
        my_queue.dequeue()
    print(f'my queue is:\n{my_queue}')
