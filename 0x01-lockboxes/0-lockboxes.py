#!/usr/bin/python3
'''this module contains a function canUnlockAll
the function takes in a list of locked boxex and finds out
if the keys to all the boxes are available in the boxes'''


def canUnlockAll(boxes, open_boxes=set(), ava_keys=None):
    '''this function tries to find out if
    all the boxes in a list can be opened simultaneously
    parameter boxes: a list of lists, each child list represents a box
    each box contains keys
    return True if all the boxes can be opened else false'''

    if not boxes:
        return False
    if not ava_keys:
        ava_keys = set(boxes[0])
    new_keys = set()
    for key in ava_keys:
        try:
            new_keys.update(boxes[key])
        except Exception as e:
            continue
    open_boxes = open_boxes | ava_keys
    ava_keys = new_keys - open_boxes
    if len(ava_keys) > 0:
        return canUnlockAll(boxes, open_boxes, ava_keys)
    else:
        for i in range(1, len(boxes)):
            if i not in open_boxes:
                return False
        return True
