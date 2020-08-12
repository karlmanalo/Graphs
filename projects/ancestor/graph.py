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
        # Vertices must be unique, so we instantiate an empty set
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Sets an edge pointing from v1 to v2. Check if both vertices are in self.vertices
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("One of those vertices doesn't exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Instantiate an empty queue object
        q = Queue()

        # Enqueue starting node
        q.enqueue(starting_vertex)

        # Create empty set to hold visited vertices
        visited = set()

        # While queue is not empty
        while q.size() > 0:
            
            # Dequeue first vertex in queue and save it to variable v
            v = q.dequeue()

            """
            If v hasn't been visited, print (visit) v. Now add all
            neighbors of v to the queue and repeat until q.size() = 0.
            """
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Instantiate an empty stack
        s = Stack()

        # Push starting vertex to stack
        s.push(starting_vertex)

        # Create empty set to hold visited vertices
        visited = set()

        # While stack is not empty
        while s.size() > 0:

            # Pop (remove the last element) of the stack and save it as q
            v = s.pop()

            """
            If v has not been visited, visit (print) it and add it to
            visited. Now get all neighbors of v and push them to the 
            stack, repeating this process until the stack is empty.
            """
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create visited set. Don't use mutable objects as default parameters!
        if visited is None:
            visited = set()

        # Visit starting_vertex and add it to visited
        print(starting_vertex)
        visited.add(starting_vertex)

        # Recursively add neighbors to visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Instantiate empty queue
        q = Queue()

        # Add starting vertex as first node in path
        q.enqueue([starting_vertex])

        # Instantiate empty set to hold visited vertices
        visited = set()

        while q.size() > 0:
            # Dequeue first path
            path = q.dequeue()

            # Get last element of path (initially the starting node) as v
            v = path[-1]

            """
            If v has not been visited, add it to visited. Check if v
            is equal to the destination_vertex. If it is, return the 
            path. Otherwise, get neighbors, append those neighbors to
            the saved path, and add that path to the queue. Repeat
            until the desired path is found or q.size == 0.
            """
            if v not in visited:
                visited.add(v)

                if v == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Instantiate empty stack
        s = Stack()

        # Push starting vertex as first node in path
        s.push([starting_vertex])

        # Instantiate empty set to hold visited vertices
        visited = set()

        while s.size() > 0:

            # Dequeue first path
            path = s.pop()

            # Get last element of path (initially the starting node) as v
            v = path[-1]

            """
            If v has not been visited, add it to visited. Check if v
            is equal to the destination_vertex. If it is, return the 
            path. Otherwise, get neighbors, add those neighbors to
            the saved path, and push that path to the stack. Repeat
            until the desired path is found or s.size == 0.
            """
            if v not in visited:
                visited.add(v)

                if v == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Create visited set. Don't use mutable objects as default parameters!
        if visited is None:
            visited = set()

        # Create empty list to hold path. Don't use mutable objects as default parameters!
        if path is None:
            path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None

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
