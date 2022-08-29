#!/usr/bin/python3
def pascal(level, column):
    if level == 1:
        return 1
    elif column == 0:
        return pascal(level - 1, column)
    elif column == level - 1:
        return pascal(level - 1, column - 1)
    else:
        return pascal(level - 1, column) + pascal(level - 1, column - 1)

def show_pascal_tree():
    pass