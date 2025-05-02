# 207. Course Schedule

# TC : O(V + E) where V is the number of vertices (courses) and E is the number of edges (prerequisites).
    # Building the graph and calculating in-degrees: O(E)
    # Finding initial courses with no prerequisites: O(V)
    # BFS traversal: O(V + E)

# SC : O(V + E)
    # Adjacency list: O(V + E)
    # In-degree array: O(V)
    # Queue: O(V) in worst case

# Did this code successfully run on Leetcode : yes

# Approach :
# Create an adjacency list representation of the graph where graph[i] contains all courses that depend on course i.
# Maintain an in-degree array to track how many prerequisites each course has.
# Build the graph and calculate in-degrees based on the prerequisites list.
# Initialize a queue with all courses that have no prerequisites (in-degree of 0).
# Use a counter to track how many courses we can take.
# Process courses in topological order using BFS:
    # Take a course from the queue (it has no remaining prerequisites)
    # Increment our count of taken courses
    # For each course that depends on the current course, reduce its prerequisite count
    # If a course now has all its prerequisites satisfied, add it to the queue
# Check if we can take all courses by comparing our count to the total number of courses.

from collections import deque
from typing import List, Optional

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list representation of the graph
        # where graph[i] contains all courses that depend on course i
        graph = [[] for _ in range(numCourses)]
        
        # Create an in-degree array to track prerequisites for each course
        in_degree = [0] * numCourses
        
        # Build the graph and calculate in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize a queue with all courses that have no prerequisites
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Count of courses that can be taken
        count = 0
        
        # Process courses in topological order
        while queue:
            # Take a course with no remaining prerequisites
            current = queue.pop(0)
            count += 1
            
            # For each course that depends on the current course
            for next_course in graph[current]:
                # Reduce its prerequisite count
                in_degree[next_course] -= 1
                # If all prerequisites are satisfied, add to queue
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If we can take all courses, return true
        return count == numCourses