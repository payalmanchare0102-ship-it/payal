class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    # a) INSERT a node
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    # b) DELETE a node
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    # Helper function to find minimum node
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # c) SEARCH a node
    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # d) TRAVERSALS
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # e) DISPLAY LEAF NODES
    def display_leaf_nodes(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(root.data, end=" ")
        self.display_leaf_nodes(root.left)
        self.display_leaf_nodes(root.right)

    # f) DISPLAY MAX & MIN
    def find_max(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.data


# ---------------------- MAIN PROGRAM ----------------------
bst = BST()
root = None

# Insert nodes
elements = [50, 30, 20, 40, 70, 60, 80]
for el in elements:
    root = bst.insert(root, el)

print("Inorder traversal:")
bst.inorder(root)

# Search a node
key = 40
print(f"\n\nSearching for {key}...")
if bst.search(root, key):
    print("Node found!")
else:
    print("Node not found!")

# Delete a node
delete_key = 30
print(f"\nDeleting node {delete_key}...")
root = bst.delete(root, delete_key)

print("Inorder traversal after deletion:")
bst.inorder(root)

# Display leaf nodes
print("\n\nLeaf nodes:")
bst.display_leaf_nodes(root)

# Display Max and Min
print(f"\n\nMinimum node value: {bst.find_min(root).data}")
print(f"Maximum node value: {bst.find_max(root)}")
