"""
This module generates a binary tree that represents a Fibonacci sequence.
"""


class TreeNode:
    """
    This class represents a node in a binary tree.
    """

    def __init__(self):
        self.left = None
        self.right = None


def fibonacci_tree(n: int) -> TreeNode:
    """
    This function recursively generates a fibonacci tree of order n.

    Args:
        n (int): The order of the Fibonacci tree.

    Returns:
        TreeNode: A node of a Fibonacci tree.
    """
    if n in (0, 1):
        return TreeNode()
    root = TreeNode()
    root.left = fibonacci_tree(n - 1)
    root.right = fibonacci_tree(n - 2)
    return root


def count_nodes(root: TreeNode) -> int:
    """
    This function counts the number of nodes in a binary tree.

    Args:
        root (TreeNode): A node of a binary tree.

    Returns:
        int: The number of nodes in a binary tree.
    """
    if root:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    return 0


def count_leaves(root: TreeNode) -> int:
    """
    This function counts the number of leaves in a binary tree.

    Args:
        root (TreeNode): A node of a binary tree.

    Returns:
        int: The number of leaves in a binary tree.
    """
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def determine_depth(root: TreeNode) -> int:
    """
    This function determines the depth of a binary tree.

    Args:
        root (TreeNode): A node of a binary tree.

    Returns:
        int: The depth of a binary tree.
    """
    if root:
        return 1 + max(determine_depth(root.left), determine_depth(root.right))
    return -1


def check_strictness(root: TreeNode) -> bool:
    """
    This function checks if a binary tree is strict.

    Args:
        root (TreeNode): A node of a binary tree.

    Returns:
        bool: A boolean value indicating whether a binary tree is strict or not.
    """
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return check_strictness(root.left) and check_strictness(root.right)
    return False


if __name__ == '__main__':
    tree = fibonacci_tree(10)
    nodes = count_nodes(tree)
    leaves = count_leaves(tree)
    depth = determine_depth(tree)
    strict = check_strictness(tree)
    print(f"Pointer to Fibonacci Tree: {repr(tree)}")
    print(f"Number of Nodes in Tree: {nodes}")
    print(f"Number of Leaves in Tree: {leaves}")
    print(f"Depth of Tree: {depth}")
    print(f"Strict Tree: {strict}")
