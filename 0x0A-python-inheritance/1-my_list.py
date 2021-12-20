#!/usr/bin/python3
'''module that creates a list subclass'''


class MyList(list):
    '''defines a list object with added methods'''
    def print_sorted(self):
        '''prints the list, sorted
        Args:
            none
        Return:
            none
        '''
        print(sorted(self))
