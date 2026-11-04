class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# 1. create the tree and give back its top node
def create_tree():
    root = Node("Director: Olena")

    it = Node("IT department")
    sales = Node("Sales department")

    root.add_child(it)
    root.add_child(sales)

    it.add_child(Node("Ivan"))
    it.add_child(Node("Maria"))
    it.add_child(Node("Petro"))

    sales.add_child(Node("Anna"))
    sales.add_child(Node("Oleh"))

    print("Tree created")
    return root


# 2. print the structure by levels
def print_levels(node, level=1):
    print(f"Level {level}: {node.value}")
    for child in node.children:
        print_levels(child, level + 1)


# 3. number of employees in each department
def count_employees(director):
    for department in director.children:
        print(f"{department.value}: {len(department.children)} employees")


# 4. employees who don't manage anyone
def print_leaves(node):
    if node.children == []:
        print(node.value)
    else:
        for child in node.children:
            print_leaves(child)


# add a new employee to a department
def add_employee(department, name):
    department.add_child(Node(name))
    print(f"Added {name} to {department.value}")


# Check 1: create the tree
tree = create_tree()

# Check 2: structure by levels
print("\nStructure:")
print_levels(tree)

# Check 3: employees per department
print("\nEmployees per department:")
count_employees(tree)

# Check 4: employees who don't manage anyone
print("\nEmployees without subordinates:")
print_leaves(tree)

# Extra: add a new employee to IT
print()
it_department = tree.children[0]
add_employee(it_department, "Sofia")

print("\nStructure after adding:")
print_levels(tree)

print("\nEmployees per department:")
count_employees(tree)