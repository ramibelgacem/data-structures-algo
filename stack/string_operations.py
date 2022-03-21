# -*- coding: utf-8 -*-

class StackError(Exception):
    pass


class CustomStack:
    """
    This stack allows as to perform some operations
    on its elements
    """
    max_value = 2 ** 10

    def __init__(self):
        self._stack = []

    def get(self):
        """Get the topmost value"""
        if not self._stack:
            raise StackError
        return self._stack[-1]

    def push(self, val):
        """Push a new value
        :param val: new value to add to the stack
        :type val: int
        """
        if val > self.max_value:
            raise StackError
        self._stack.append(val)

    def pop(self):
        """Delete the topmost value"""
        val = self.get()
        del self._stack[-1]
        return val

    def addition(self):
        """Add the topmost elements"""
        self.push(self.pop() + self.pop())

    def substruct(self):
        """Substruct the topmost elements"""
        self.push(self.pop() - self.pop())

    def duplicate(self):
        """Duplicate the topmost element"""
        self.push(self.get())


def main(operations):
    number_stack = CustomStack()
    try:
        for operation in operations.split(' '):
            try:
                new_value = int(operation)
                number_stack.push(new_value)
            except ValueError:
                if operation == '+':
                    number_stack.addition()
                elif operation == '-':
                    number_stack.substruct()
                elif operation == 'DUP':
                    number_stack.duplicate()
                elif operation == 'POP':
                    number_stack.pop()
                else:
                    pass

        return number_stack.get()
    except StackError:
        return -1


if __name__ == '__main__':
    print(main("5 6 DUP POP 1 + 8 -"))
