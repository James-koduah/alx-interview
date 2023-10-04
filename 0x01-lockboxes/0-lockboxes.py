#!/usr/bin/python3
"""An alx interveiw question where we have to solve the problem of lockboxes"""

def canUnlockAll(boxes):
    """Let's see if we can unlock all boxes"""
    search = True
    keys = []
    opened_boxes = [0]
    for elem in boxes[0]:
        keys.append(elem)
    """
    for key in keys:
        if key in opened_boxes:
            continue
        for elem in boxes[key]:
            keys.append(elem)
            opened_boxes.append(key)
    print(opened_boxes)
    """
    while search:
        for key in keys:
            search = False
            if key in opened_boxes:
                pass
            else:
                if key < len(boxes):
                    opened_boxes.append(key)
                    for elem in boxes[key]:
                        keys.append(elem)
                    search = True
    if len(opened_boxes) == len(boxes):
        return True
    else:
        return False
