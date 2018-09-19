def BooleanNOT(x):
    # not x
    if x:
        return False
    else:
        return True


def BooleanOR(x, y):
    # x or y
    if not x:
        return y
    else:
        return x

def BooleanAND(x, y):
    # x and y
    if not x:
        return x
    else:
        return y
