#!/usr/bin/python3
'''Module to create a singly linked list data structure and manipulate them'''


class Node:
    '''The node class'''
    def __init__(self, data, next_node=None) -> object:
        '''the class constructor
        Args:
            data(int): the node data
            next_node(Node): the next node
        Return:
            Node object
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''getter for data property
        Args:
            none
        Return:
            int: the node data
        the setter method
        Args:
            value(int): the int data to be stored
        Return: nothing
        '''
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''getter for the next_node property
        Args:
            none
        Return:
            Node: the next node
        setter method
        Args:
            value(Node): the node to be set as the next node
        Return:
            nothing
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''class to define a singly linked list'''
    def __init__(self):
        self.__head = None

    def __str__(self):
        '''str representation of a sll.
        Return:
            str: a string that contains datas of all nodes in the list
            separated by a new line
        '''
        current = self.__head
        rep_str = ""
        while current:
            rep_str += str(current.data)
            if current.next_node:
                rep_str += "\n"
            current = current.next_node
        return rep_str

    def sorted_insert(self, value):
        '''inserts a new node, sorting them by the data they contain
        Args:
            value(int): value of the new node
        Return:
            nothing
        '''
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        current = self.__head
        previous = None
        while current:
            if value <= current.data:
                break
            previous = current
            current = previous.next_node
        if previous:
            previous.next_node = new
        else:
            self.__head = new
        new.next_node = current
