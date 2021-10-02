from dataclasses import dataclass, field
from itertools import tee
from typing import TypeVar

T = TypeVar("T")


@dataclass
class Node:
    value: T = None
    next_node: "Node" = None
    past_node: "Node" = None

    @staticmethod
    def sential_node() -> 'Node':
        return Node(None)


class ValueNotFoundException(RuntimeError):
    def __init__(self, value: T):  # pragma: nocover
        super().__init__(f"Value: {value} not found in list")


@dataclass
class LinkedList:
    _count: int = 0
    # Factory for sential head
    _head: Node = field(default_factory=Node.sential_node)
    _tail: Node = None

    def __post_init__(self):
        self._tail = self._head

    def __iter__(self):
        current_node = self._head.next_node
        while current_node:
            yield current_node
            current_node = current_node.next_node

    def __len__(self):
        return self._count

    def __contains__(self, value: T) -> bool:
        current_node = self._head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def push_front(self, value: T):
        new_node = Node(value)
        new_node.next_node = self._head.next_node
        self._head.next_node = new_node

    def get_largest_item(self):
        largest_item = self._head.next_node
        for node in self:
            if node.value > largest_item.value:
                largest_item = node
        return largest_item.value

    def insert(self, value: T):
        new_node = Node(value)
        self._tail.next_node = new_node
        self._tail = self._tail.next_node
        self._count += 1

    def delete(self, value: T):
        current_node = self._head
        while current_node.next_node:
            if current_node.next_node.value == value:
                deleted_node = current_node.next_node
                current_node.next_node = deleted_node.next_node
                self._count -= 1
                if deleted_node == self._tail:
                    self._tail = current_node
                return
            current_node = current_node.next_node
        raise ValueNotFoundException(value)  # pragma: nocover

    def find(self, value: T) -> int:
        for index, node in enumerate(self):
            if node.value == value:
                return index
        raise ValueNotFoundException(value)  # pragma: nocover

    @property
    def sorted(self) -> bool:
        iter_list = iter(self)
        for node_i in iter_list:
            for node_j in tee(iter_list, 1)[0]:
                if node_i.value > node_j.value:
                    return False
        return True


@dataclass
class DoublyLinkedList(LinkedList):

    def push_front(self, value: T):
        super().push_front(value)
        new_node = self._head.next_node
        new_node.past_node = self._head
        new_node.next_node.past_node = new_node

    def insert(self, value: T):
        new_node = Node(value)
        self._tail.next_node = new_node
        new_node.past_node = self._tail
        self._tail = self._tail.next_node

    def delete(self, value: T):
        current_node = self._head
        while current_node.next_node:
            if current_node.next_node.value == value:
                deleted_node = current_node.next_node
                current_node.next_node = deleted_node.next_node
                self._count -= 1
                if deleted_node == self._tail:
                    self._tail = current_node
                else:
                    deleted_node.next_node.past_node = deleted_node.past_node
                return
            current_node = current_node.next_node
        raise ValueNotFoundException(value)  # pragma: nocover
