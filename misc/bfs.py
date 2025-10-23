
from  collections import defaultdict

input = ['Kitchen-LivingRoom', 'Bedroom-Bathroom', 'LivingRoom-Bedroom']
start_room = 'Kitchen'
end_room = 'Bathroom'

def build_graph(connections):
    graph = defaultdict(list)
    for c in connections:
        room1, room2 = c.split('-')
        graph[room1].append(room2)
        graph[room2].append(room1)
    return graph

def find_shortest_path(graph, start, end):
    from collections import deque

    queue = deque([(start, [start])])
    visited = {start}

    while (queue):
        current_room, path = queue.popleft()
        if current_room == end:
            return path
        for neighbor in graph[current_room]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

graph = build_graph(input)
shortest_path = find_shortest_path(graph, start_room, end_room)
print("Shortest path from", start_room, "to", end_room, "is:", shortest_path)
