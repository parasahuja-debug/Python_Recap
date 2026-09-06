# Given an integer n, return the number of structurally unique BST's 
# (binary search trees) that store values 1 to n.

# Input: n = 3
# Output: 5
# (There are 5 distinct BST shapes using values 1, 2, 3.)
def num_trees_memo(number_of_nodes: int) -> int:
    memo = {}

    def solve(nodes: int) -> int:
        if nodes <= 1:
            return 1
        if nodes in memo:
            return memo[nodes]

        total_trees = 0
        for root_position in range(1, nodes + 1):
            left_subtree_size = root_position - 1
            right_subtree_size = nodes - root_position
            total_trees += solve(left_subtree_size) * solve(right_subtree_size)

        memo[nodes] = total_trees
        return total_trees

    return solve(number_of_nodes)