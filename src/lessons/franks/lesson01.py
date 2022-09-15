#!/usr/bin/env python
# -*- coding: utf-8 -*-

valid_html = """
<html>
<h1>
blah
<h2>
</h2>
</h1>
</html>
"""

invalid_html = """
<html>
</h1>
</h1>
"""


class Stack():

    def __init__(self):
        self.the_stack = []
        self.size = len(self.the_stack)

    def push(self, stack_item):
        self.size += 1
        self.the_stack.append(stack_item)

    def pop(self):
        if not self.is_empty():
            last_in = self.the_stack[-1]
            del self.the_stack[-1]
            return last_in
        return None

    def peek(self):
        return self.the_stack[-1]

    def size(self):
        self.size == len(self.the_stack)
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False


def html_checker(html):
    checker = Stack()
    for line in html.split("\n"):
        if "</" in line:
            if checker.is_empty():
                return False
            elif ">" in line:
                tag = checker.pop()
                if line[2:-1] != tag:
                    return False
        elif "<" in line:
            if ">" in line:
                checker.push(line[1:-1])
    return True


for html in [valid_html, invalid_html]:
    print(html_checker(html))
