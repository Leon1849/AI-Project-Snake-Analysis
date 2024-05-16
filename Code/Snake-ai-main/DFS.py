from Utility import Node
from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)
        self.frontier = []

    def recursive_DFS(self, snake, goal_state, current_state):
        if current_state.equal(goal_state):
            return self.get_path(current_state)

        if current_state in self.explored_set:
            return None

        self.explored_set.append(current_state)

        for neighbor in self.get_neighbors(current_state):
            if self.is_valid_move(snake, neighbor) and neighbor not in self.explored_set:
                self.frontier.append(neighbor)
                neighbor.parent = current_state
                path = self.recursive_DFS(snake, goal_state, neighbor)
                if path:
                    return path

        return None

    def run_algorithm(self, snake):
        if self.path:
            next_step = self.path.pop()
            if self.is_valid_move(snake, next_step):
                return next_step

        self.frontier.clear()
        self.explored_set = []
        self.path = []

        initial_state, goal_state = self.get_initstate_and_goalstate(snake)

        return self.recursive_DFS(snake, goal_state, initial_state)

    def is_valid_move(self, snake, node):
        return not self.inside_body(snake, node) and not self.outside_boundary(node)