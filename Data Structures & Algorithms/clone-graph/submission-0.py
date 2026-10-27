"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque()
        q.append(node)
        mp = {node: Node(node.val)}

        while q:
            curr = q.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in mp:
                    mp[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                mp[curr].neighbors.append(mp[neighbor])
        
        return mp[node]

            
                
    
        
