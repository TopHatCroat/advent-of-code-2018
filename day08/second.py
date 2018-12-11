from collections import namedtuple
from typing import List

class Node():
    def __init__(self, num_children: int, num_meta: int, children: List, meta: List[int]) -> None:
        self.num_children = num_children
        self.num_meta = num_meta
        self.children = children
        self.meta = meta

def populate(numbers):
    node = Node(numbers.pop(0), numbers.pop(0), [], [])

    for i in range(node.num_children):
        node.children += [ populate(numbers) ]

    for i in range(node.num_meta):
        node.meta += [ numbers.pop(0) ]

    return node

def count_meta_with_children(node):
    if node.num_children == 0:
        count = sum(node.meta)
    else:
        count = 0
        for i in node.meta:
            if i - 1 < node.num_children:
                count += count_meta_with_children(node.children[i - 1])

    return count

numbers = [ int(x) for x in open("input.txt").read().strip().split(" ") ]

tree = populate(numbers)

print(count_meta_with_children(tree))
    