from collections import defaultdict
from collections import deque

def top_view(root):
    if not root:
        return []
    result = []
    queue = deque([(root,0)])
    horizontal_distance_map = defaultdict(lambda:None)
    while queue:
        current_node, hd = queue.popleft()
        if hd not in horizontal_distance_map:
            horizontal_distance_map[hd] = current_node
            result.append(current_node.data)
        if current_node.left:
            queue.append((current_node.left,hd-1))
        if current_node.right:
            queue.append((current_node.left,hd+1))
    return result