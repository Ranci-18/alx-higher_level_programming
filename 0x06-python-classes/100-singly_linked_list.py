#!/usr/bin/python3
"""Defining Classes node and singly linked list"""


class Node:
    """Node class with attributes

    Attributes: data and next_node
    """
    def __init__(self, data, next_node=None):
        """Attribute instantiation
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Property getter of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter of data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Property getter of next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter of next_node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class with head attribute
    """
    def __str__(self):
        """Class object as a string

        Return: the string
        """
        mt = ""
        hd = self.__head

        while hd is not None:
            mt += str(hd.data)
            if hd.next_node is not None:
                mt += "\n"
            hd = hd.next_node

        return mt

    def __init__(self):
        """Instantiation of head attribute
        """
        self.__head = None

    def sorted_insert(self, value):
        """Method to add new_node
        """
        hd = self.__head

        while hd is not None:
            if hd.data > value:
                break
            hd_prev = hd
            hd = hd.next_node

        new_node = Node(value, hd)
        if hd == self.__head:
            self.__head = new_node
        else:
            hd_prev.next_node = new_node
