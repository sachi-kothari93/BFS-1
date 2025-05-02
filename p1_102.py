# 102. Binary Tree Level Order Traversal

# TC : O(n) where n is the number of nodes
# SC : O(n) in the worst case. The queue could contain all nodes in the last level, which could be up to n/2 nodes in a complete binary tree
# Did this code successfully run on Leetcode : yes

# Approach :
# Queue-based BFS traversal: Use a queue data structure to process nodes level by level, starting from the root and moving downward.
# Level tracking: Keep track of how many nodes are at each level by measuring the queue size before processing that level's nodes.
# Batch processing: Process all nodes at the current level before moving to the next level, which ensures nodes are grouped correctly by level.
# Result construction: For each level, collect all node values in a separate list, then add that list to the final result, creating a list of lists structure.
# The algorithm follows these steps:
    # Start with the root node in the queue
    # For each level, determine how many nodes need to be processed
    # Process each node at the current level, adding its children to the queue for future processing
    # Group all node values from the current level together
    # Repeat until the queue is empty (all levels processed)
# This approach guarantees the traversal maintains both the level grouping and the left-to-right ordering within each level as required by the problem.

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
            
        # Initialize result list and deque for BFS
        result = []
        queue = deque([root])
        
        # BFS traversal
        while queue:
            # Current level values
            level_values = []
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                # Get the next node from queue (O(1) operation)
                node = queue.popleft()
                
                # Add node's value to current level
                level_values.append(node.val)
                
                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add current level values to result
            result.append(level_values)
        
        return result