import json


def TreeConstructor(strArr):
    result = []
    for x in strArr:
        result.append(eval(x))

    head = []
    tree = {}
    for x in result:
        head.append(x[1])
        tree[x[1]] = []
    head = list(set(head))
    for x in result:
        if x[0] in head:
            head.remove(x[0])
    if len(head) != 1:
        return False
    head = head[0]

    for x in result:
        tree[x[1]].append(x[0])
    for item, key in enumerate(tree):
        if len(tree[key]) > 2:
            return False
    return True


# keep this function call here
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))
