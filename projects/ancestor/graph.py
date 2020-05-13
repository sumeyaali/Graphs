"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if edge exists
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('error: This is not available')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #Create the queue and enque the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()
        while q.size() > 0:
            #create the path 
            path = q.dequeue()
            #Once we dequeue, we check to see if the last number in the list has been visited
            if path[-1] not in visited:
            #DO THE THING
                print(path[-1])
                visited.add(path[-1])

                for next_edge in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_edge)
                    q.enqueue(new_path)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()
        while s.size() > 0:
            #create the path 
            path = s.pop()
            #Once we dequeue, we check to see if the last number in the list has been visited
            if path[-1] not in visited:
            #DO THE THING
                print(path[-1])
                visited.add(path[-1])

                for next_edge in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_edge)
                    s.push(new_path)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        s.push([starting_vertex])

        if visited is None:
            visited = set()     
        #Do the thing
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited )

           


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Create the queue and enque the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()
        while q.size() > 0:
            #create the path 
            path = q.dequeue()
            #Once we dequeue, we check to see if the last number in the list has been visited
            if path[-1] not in visited:
            #DO THE THING
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])

                for next_edge in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_edge)
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()
        while s.size() > 0:
            #create the path 
            path = s.pop()
            #Once we dequeue, we check to see if the last number in the list has been visited
            if path[-1] not in visited:
            #DO THE THING
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])

                for next_edge in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_edge)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()
        s.push([starting_vertex])

        if visited is None:
            visited = set()  

        if path is None:
            path = []   
        #Do the thing     
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if path[-1] == destination_vertex:
            return path
      
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_neighbor = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_neighbor:
                    return new_neighbor

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
