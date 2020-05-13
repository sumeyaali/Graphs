'''
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9

    
'''
from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):   
    graph = Graph()
    for element in ancestors:
        parent = element[0]
        child = element[1]

        graph.add_vertex(parent)
        graph.add_vertex(child)
        
        graph.add_edge(child, parent)
        


    s = Stack()
    s.push([starting_node])
    ancestor_path= []

    visited = set()
    while s.size() > 0:
        #create the path 
        path = s.pop()
        print(path)
        #Once we dequeue, we check to see if the last number in the list has been visited
        if path[-1] not in visited:
        #DO THE THING
            if len(path) > len(ancestor_path):
                ancestor_path = path
            visited.add(path[-1])

            if len(path) == len(ancestor_path):
                if path[-1] < ancestor_path[-1]:
                    ancestor_path = path



            for next_edge in graph.get_neighbors(path[-1]):
                new_path = list(path)
                print(new_path)
                new_path.append(next_edge)
                s.push(new_path)
    print(ancestor_path[-1])
    if len(ancestor_path) == 1:
        return -1
    return ancestor_path[-1]
        