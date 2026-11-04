class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# 1. create the tree and give back its top node
def create_tree():
    root = Node("Python")

    basics = Node("Basics")
    oop = Node("OOP")
    projects = Node("Projects")

    root.add_child(basics)
    root.add_child(oop)
    root.add_child(projects)

    basics.add_child(Node("variables.py"))
    basics.add_child(Node("loops.py"))

    oop.add_child(Node("classes.py"))
    oop.add_child(Node("inheritance.py"))

    projects.add_child(Node("calculator.py"))
    projects.add_child(Node("todo_app.py"))

    print("Tree created")
    return root


# 2. print the names of all nodes
def print_all(node):
    print(node.value)
    for child in node.children:
        print_all(child)


# 3. show the children of a node
def show_children(node):
    for child in node.children:
        print(child.value)


# 4. find the leaves
def print_leaves(node):
    if node.children == []:
        print(node.value)
    else:
        for child in node.children:
            print_leaves(child)


# Check 1: create the tree
tree = create_tree()

# Check 2: all nodes
print("\nAll nodes:")
print_all(tree)

# Check 3: children of OOP
print("\nChildren of OOP:")
oop_folder = tree.children[1]
show_children(oop_folder)

# Check 4: leaves
print("\nLeaves:")
print_leaves(tree)