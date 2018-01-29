class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)
d.neighbors.add(c)
e.neighbors.add(d)
a.neighbors.add(e)

graph = [a, b, c, d, e]

def validColoring(graph):
    for node in graph:
    	for neighbor in node.neighbors:
    		if not node.color or not neighbor.color or node.color == neighbor.color:
    			return False
    return True

def colorations(graph, colors):
    if len(graph) == 1:
        return [[x] for x in range(0, colors)]
    else:
        res = []
        sols = colorations(graph[1:], colors)
        for i in range(0, colors):
            for sol in sols:
                res.append([i] + sol)
        return res

def bruteForceColoring(graph):
    all_colorations = colorations(graph, len(graph))
    for cur_coloration in all_colorations:
        for i, node in enumerate(graph):
            node.color = cur_coloration[i]
        if validColoring(graph):
            return cur_coloration


print bruteForceColoring(graph)
