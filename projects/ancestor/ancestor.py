from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):

    # Instantiate family tree as an empty Graph instance
    family_tree = Graph()

    # Add all nodes as vertices to family_tree
    for pair in ancestors:
        family_tree.add_vertex(pair[0])
        family_tree.add_vertex(pair[1])

    # Add edges from ancestors
    for pair in ancestors:
        family_tree.add_edge(pair[1], pair[0])

    # BFS to find furthest "ripple". Instantiate empty queue
    q = Queue()

    # Enqueue starting node as 1-element list
    q.enqueue([starting_node])

    # Create empty visited set
    visited = set()

    # Default parameters for max_path_length and earliest_ancestor
    max_path_length = 1
    earliest_ancestor = -1

    # While the queue is not empty
    while q.size() > 0:
        # Dequeue the path at index 0 and save it as variable path
        path = q.dequeue()

        # Save the final vertex in the saved path to variable v
        v = path[-1]

        # If v hasn't been visited, add it to the visited set
        if v not in visited:
            visited.add(v)

        """
        Checking two conditionals here. The first conditional is the
        case where the path is longer than our currently saved 
        max_path_length, meaning we've found an earlier ancestor than 
        our currently saved ancestor, meaning we should overwrite our 
        default values. The second conditional checks that the path 
        length is greater than or equal to the currently saved 
        max_path_length (to ensure that the current path is indeed the 
        earliest ancestor) AND that v is less than the currently saved 
        earliest_ancestor (to ensure the value of v is the lowest 
        indexed parent). If either of these conditionals are met, we 
        overwrite our currently saved earliest_ancestor and 
        max_path_length variables.
        """
        if len(path) > max_path_length or (len(path) >= max_path_length and v < earliest_ancestor):
            earliest_ancestor = v
            max_path_length = len(path)

        # Repeat this process for all neighbors if they haven't been visited
        for neighbor in family_tree.get_neighbors(v):
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return earliest_ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))