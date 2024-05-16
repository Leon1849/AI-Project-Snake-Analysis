from collections import deque
from Utility import Node
from Algorithm import Algorithm
#new for Best First
import heapq


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)
        self.visited = set()

    def run_algorithm(self, snake):
        self.frontier.clear()
        self.explored_set.clear()
        self.path.clear()
        self.visited.clear()

        init_state, goal_state = self.get_initstate_and_goalstate(snake)
        
        self.frontier.append((init_state, 0))

        while self.frontier:
            current_node, _ = self.frontier.pop(0)

            if current_node.equal(goal_state):
                return self.get_path(current_node)

            self.explored_set.append(current_node)

            for neighbor in self.get_neighbors(current_node):
                if neighbor not in self.explored_set and not self.inside_body(snake, neighbor) and not self.outside_boundary(neighbor):
                    cost = self.manhattan_distance(neighbor, goal_state)
                    if (neighbor, cost) not in self.frontier and neighbor not in self.visited:
                        self.frontier.append((neighbor, cost))
                        neighbor.parent = current_node
                        self.visited.add(neighbor)

            self.frontier.sort(key=lambda x: x[1])

        return []
