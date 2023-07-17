class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def parse_data(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.right = TreeNode(parse_data(data[2]))
        node.left = TreeNode(parse_data(data[0]))

    elif data is None:
        node = None

    else:
        node = TreeNode(data)

    return node


data = ((0, 1, 2), 2, (2, 3, 5))

tree2 = parse_data(data)
print(tree2)


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if not node:
        return None, None

    min_l, max_l = is_bst(node.left)
    min_r, max_r = is_bst(node.right)

    is_the_bst = True

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return min_key, max_key


is_bst(tree2)