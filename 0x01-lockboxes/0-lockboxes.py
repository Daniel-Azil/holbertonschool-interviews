#!/usr/bin/python3
"""
A module determines if given boxes can be opened.
"""


def canUnlockAll(boxes):
    """ A function method that determines if all the boxes can be opened.
    """

    if boxes is None:
        return False
    if not isinstance(boxes, list):
        return False
    if boxes == []:
        return False
    if boxes == [[]]:
        return True
    if boxes[0] == [] and len(boxes) > 1:
        return False
    for ele in boxes:
        if not isinstance(ele, list):
            return False
        else:
            for val in ele:
                if not isinstance(val, int):
                    return False
    stg = [False for ele in boxes]
    stg[0] = True
    ent = [False for ele in boxes]
    while [True for ele in range(len(boxes))
           if ent[ele] is False and stg[ele] is True]:
        for i in range(len(boxes)):
            if stg[i] is True:
                ent[i] = True
                for ele in boxes[i]:
                    try:
                        stg[ele] = True
                    except:
                        pass
    return False not in stg
