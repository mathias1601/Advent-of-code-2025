nodes_dict = {}

with open("input11.txt") as f:

    for line in f:
        line = line.strip("\n")
        line = line.split(" ")
        nodes_dict[line[0].strip(":")] = line[1:]

paths = []

# Method does not account for infinite loops, but can do so by not allowing moving to nodes which are in visited_nodes
def recursive_path_search(nodes_dict, current_node, visited_nodes):
    
    for node in nodes_dict.get(current_node):
        visited_nodes.append(node)
        if node == "out":
            paths.append(visited_nodes)
            return
        recursive_path_search(nodes_dict, current_node=node, visited_nodes=visited_nodes)
        

recursive_path_search(nodes_dict, "you", [])
print(len(paths))