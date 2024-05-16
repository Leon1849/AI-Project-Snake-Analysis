from Algorithm import Algorithm
from Constants import *
import heapq

class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        initial_state, goal_state = self.get_initstate_and_goalstate(snake)
        self.frontier = [(0, initial_state)]
        self.explored_set = set()

        while self.frontier:
            _, current_node = heapq.heappop(self.frontier)

            if current_node.equal(goal_state):
                return self.get_path(current_node)

            self.explored_set.add(current_node)
            self.process_neighbors(current_node, goal_state, snake)

        return None

    def process_neighbors(self, node, goal_state, snake):
        for neighbor in self.get_neighbors(node):
            if neighbor in self.explored_set or not self.is_safe_move(neighbor, snake):
                continue

            new_g = node.g + 1
            if new_g < neighbor.g or neighbor not in [n[1] for n in self.frontier]:
                neighbor.update_node(node, new_g, self.manhattan_distance(goal_state, neighbor))
                heapq.heappush(self.frontier, (neighbor.f, neighbor))

    def is_safe_move(self, node, snake):
        return 0 <= node.x < NO_OF_CELLS and 0 <= node.y < NO_OF_CELLS and \
               all(node.x != segment.x or node.y != segment.y for segment in snake.body)
