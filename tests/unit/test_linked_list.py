from algos import linked_list

import pytest


# Linked List

def test_linked_list_insert():
    my_linked_list = linked_list.LinkedList()
    my_linked_list.insert("hello")
    my_linked_list.insert("world")
    my_linked_list.insert("my")
    my_linked_list.insert("name")
    my_linked_list.insert("is")
    assert len(my_linked_list) == 5


def test_linked_list_contains():
    my_linked_list = linked_list.LinkedList()
    my_linked_list.insert(2)
    assert 2 in my_linked_list


@pytest.fixture(scope="function")
def loaded_linked_list() -> linked_list.LinkedList:
    my_linked_list = linked_list.LinkedList()
    my_linked_list.insert("hello")
    my_linked_list.insert("world")
    my_linked_list.insert("my")
    my_linked_list.insert("name")
    my_linked_list.insert("is")
    return my_linked_list


def test_linked_push_front(loaded_linked_list: linked_list.LinkedList):
    loaded_linked_list.push_front("First")
    iter_list = iter(loaded_linked_list)
    assert next(iter_list).value == "First"
    assert next(iter_list).value == "hello"


def test_linked_list_delete(loaded_linked_list: linked_list.LinkedList):
    loaded_linked_list.delete("my")
    assert "my" not in loaded_linked_list


def test_linked_list_delete_tail(loaded_linked_list: linked_list.LinkedList):
    loaded_linked_list.delete("is")
    assert "is" not in loaded_linked_list
    assert loaded_linked_list._tail.value == "name"


def test_linked_list_find(loaded_linked_list: linked_list.LinkedList):
    assert loaded_linked_list.find("world") == 1


def test_linked_list_get_largest_item(
    loaded_linked_list: linked_list.LinkedList
):
    assert loaded_linked_list.get_largest_item() == "world"


@pytest.mark.parametrize("values,expected", [
    ([1, 2, 3, 4, 5], True),
    ([3, 1, 4, 2, 5], False)
])
def test_linked_list_sorted(values, expected):
    my_list = linked_list.LinkedList()
    for item in values:
        my_list.insert(item)
    assert my_list.sorted == expected


# DoublyLinkedList

@pytest.fixture
def loaded_doubly_linked_list() -> linked_list.DoublyLinkedList:
    my_linked_list = linked_list.DoublyLinkedList()
    my_linked_list.insert("hi")
    my_linked_list.insert("my")
    my_linked_list.insert("name")
    return my_linked_list


def test_double_linked_list_insert(loaded_doubly_linked_list):
    expected = [None, "hi", "my"]
    for node in loaded_doubly_linked_list:
        assert node.past_node.value == expected.pop(0)


def test_double_linked_pop_front(loaded_doubly_linked_list):
    loaded_doubly_linked_list.push_front("test")
    iter_list = iter(loaded_doubly_linked_list)
    assert next(iter_list).past_node == loaded_doubly_linked_list._head
    assert next(
        iter_list).past_node == loaded_doubly_linked_list._head.next_node


@pytest.mark.parametrize("deleted,expected", [
    ("my", [None, "hi"]),
    ("hi", [None, "my"]),
    ("name", [None, "hi"])
])
def test_double_linked_list_delete(
    deleted,
    expected,
    loaded_doubly_linked_list
):
    loaded_doubly_linked_list.delete(deleted)
    assert deleted not in loaded_doubly_linked_list

    for node in loaded_doubly_linked_list:
        assert node.past_node.value == expected.pop(0)
