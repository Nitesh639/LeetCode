class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


Node1 = TreeNode(3)
Node2 = TreeNode(4)
Node3 = TreeNode(5)

Node1.left = Node2
Node1.right = Node3


# tree = Node1


def pars_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = pars_tuple(data[0])
        node.right = pars_tuple(data[2])

    elif data is None:
        node = None

    else:
        node = TreeNode(data)

    return node


data = ((1, 2, None), 2, (2, 3, None))

tree2 = pars_tuple(data)


def display_key(node, spaces='\t', level=0):
    if node is None:
        print(spaces * level + '#')
        return
    if node.left is None and node.right is None:
        print(spaces * level, node.key)
        return
    display_key(node.right, spaces, level + 1)
    print(spaces * level, node.key)
    display_key(node.left, spaces, level + 1)


display_key(tree2)


def traverse_in_order(node):
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)


print(traverse_in_order(tree2))


def traverse_pre_order(node):
    if node is None:
        return []
    return [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right)


print(traverse_pre_order(tree2))


def post_order_traverse(node):
    if node is None:
        return []
    return post_order_traverse(node.left) + post_order_traverse(node.right) + [node.key]


print(post_order_traverse(tree2))


# height of the binary tree
def height_tree(node):
    if node is None:
        return 0
    return 1 + max(height_tree(node.left), height_tree(node.right))


print(height_tree(tree2))


# for the size of binary search tree
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


print(tree_size(tree2))
