import heapq

def shortest_time_to_vaccine(n, m, new_portals, new_demon_times):
    # Create an adjacency list to represent the multiverse with portals
    graph = [[] for _ in range(n)]
    for a, b, c in new_portals:
        graph[a - 1].append((b - 1, c))
        graph[b - 1].append((a - 1, c))
    
    # Initialize a list to track the shortest time to reach each universe
    shortest_time = [float('inf')] * n
    shortest_time[0] = 0
    
    # Initialize a priority queue for Dijkstra's algorithm
    pq = [(0, 0)]  # (time, universe)
    
    while pq:
        current_time, current_universe = heapq.heappop(pq)
        
        # Check if we have reached the nth universe
        if current_universe == n - 1:
            return current_time
        
        # Check for the next possible universes to visit
        for neighbor, travel_time in graph[current_universe]:
            # Calculate the waiting time due to demons
            waiting_time = 0
            for demon_time in new_demon_times[neighbor]:
                if demon_time >= current_time + waiting_time:
                    break
                waiting_time += 1
            
            # Calculate the total time to reach the neighbor universe
            total_time = current_time + waiting_time + travel_time
            
            # Update the shortest time if it's shorter
            if total_time < shortest_time[neighbor]:
                shortest_time[neighbor] = total_time
                heapq.heappush(pq, (total_time, neighbor))
    
    # If we can't reach the nth universe, return -1
    return -1

# Read input
n, m = map(int, input().split())
new_portals = [list(map(int, input().split())) for _ in range(m)]
new_demon_times = [list(map(int, input().split()))[1:] for _ in range(n)]

# Calculate and print the shortest time
result = shortest_time_to_vaccine(n, m, new_portals, new_demon_times)
print(result)

#INPUT
# 4 4 
# 1 2 3
# 1 3 2 
# 2 4 2
# 3 4 3 
# 0
# 1 4 
# 2 2 3
# 0

#OUTPUT
#5