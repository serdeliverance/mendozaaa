#!/usr/bin/python3
def pascal_value(level, column):
    if level == 1:
        return 1
    elif column == 0:
        return pascal_value(level - 1, column)
    elif column == level - 1:
        return pascal_value(level - 1, column - 1)
    else:
        return pascal_value(level - 1, column) + pascal_value(level - 1, column - 1)