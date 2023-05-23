
class Tree:
    def __init__(self, root):
        self.root = root

    # for representing the tree in the most naive way
    def __str__(self):
        data = [[self.root]]

        # traversing the first nodes
        x = []
        for node in self.root.children:
            x.append(node)
        data.append(x)

        # for traversing the latter nodes
        def traverse_latter(nodes):
            ans = []
            flag = False
            for n in nodes:
                
                if n.children != []:
                    flag = True
                for c in n.children:
                    ans.append(c)
            return [ans, flag]
        
        # traversing the nodes after first nodes
        x = traverse_latter(data[-1])
        data.append(x[0])
        while True:
            x = traverse_latter(data[-1])
            data.append(x[0])
            if x[-1]:
                break

        # I get the values of my retrieved data and format it in a somewhat of a nice way
        decoded = []
        for nodes in data:
            x = []
            for node in nodes:
                if node.parent != None:
                    x.append(f"[{node.parent.value}]-->{node.value}")
                else:
                    x.append(f"None-->{[self.root.value]}")
            decoded.append(x)
        return str(decoded)


class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.children = []

    def add_node(self, node):
        self.children.append(node)


root = Node(None, 1)
tree = Tree(root)
node1 = Node(root, 2)
node2 = Node(root, 3)
node3 = Node(root, 4)
root.add_node(node1)
root.add_node(node2)
root.add_node(node3)

node4 = Node(node3, 5)
node3.add_node(node4)


node5 = Node(node3, 6)
node3.add_node(node5)

node6 = Node(node2, 7)
node2.add_node(node6)

node7 = Node(node6, 8)
node6.add_node(node7)

node8 = Node(node6, 9)
node6.add_node(node8)

print(tree)
