# Using Adjacency list '
class graph:
    def __init__(self):
        self.number_of_nodes = 0 
        self.adjacent_list = {} 
    
    def add_vertex(self, node):
        if node not in self.adjacent_list:
            self.adjacent_list[node] = []
            self.number_of_nodes += 1
    
    def add_edge(self, node_1, node_2):
        if node_1 not in self.adjacent_list.get(node_2):
            self.adjacent_list[node_1].append(node_2)
            self.adjacent_list[node_2].append(node_1)

    def show_connections(self):
        for item in self.adjacent_list:
            print(f"{item} --->", *self.adjacent_list.get(item))

    
my_graph = graph()
my_graph.add_vertex("0")
my_graph.add_vertex("1")
my_graph.add_vertex("2")
my_graph.add_vertex("3")
my_graph.add_vertex("4")
my_graph.add_vertex("5")
my_graph.add_vertex("6")
my_graph.add_edge("3", "1")
my_graph.add_edge("3", "4")
my_graph.add_edge("4", "2")
my_graph.add_edge("4", "5")
my_graph.add_edge("1", "2")
my_graph.add_edge("1", "0")
my_graph.add_edge("0", "2")
my_graph.add_edge("6", "5")
my_graph.show_connections()


