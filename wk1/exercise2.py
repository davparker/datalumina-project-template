"""
Exercise 2
0.0/10.0 points (graded)
Consider our representation of permutations of students in a line from Exercise 1. (The teacher only swaps the positions of two students that are next to each other in line.) Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C). Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1: vertices represent permutations of the students in line; edges connect two permutations if one can be made into the other by swapping two adjacent students.

We construct our graph by first adding the following nodes:"""

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

# Add edges between nodes (students) swapping adjacent students
# Only add one direction since Graph class automatically adds reverse edges
g.addEdge(Edge(nodes[0], nodes[1]))  # ABC->ACB (also creates ACB->ABC)
g.addEdge(Edge(nodes[0], nodes[2]))  # ABC->BAC (also creates BAC->ABC)
g.addEdge(Edge(nodes[1], nodes[4]))  # ACB->CAB (also creates CAB->ACB)
g.addEdge(Edge(nodes[2], nodes[3]))  # BAC->BCA (also creates BCA->BAC)
g.addEdge(Edge(nodes[3], nodes[5]))  # BCA->CBA (also creates CBA->BCA)
g.addEdge(Edge(nodes[4], nodes[5]))  # CAB->CBA (also creates CBA->CAB)
print(g)
