# 865. Smallest Subtree with all the Deepest Nodes

**Difficulty:** Medium

## Problem Description

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

## Examples

### Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2. The nodes 7 and 4 are the deepest nodes in the tree,
and node 2 is the smallest subtree that contains both of them.
```

### Example 2:
```
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
```

### Example 3:
```
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2.
```

## Constraints

- The number of nodes in the tree will be in the range [1, 500].
- 0 <= Node.val <= 500
- The values of the nodes in the tree are unique.

## Solution Approach

### Strategy

The key insight is to use a depth-first search (DFS) that returns both:
1. The depth of the deepest node in each subtree
2. The lowest common ancestor (LCA) of all deepest nodes in that subtree

For each node, we:
- Recursively compute the depth and LCA for both left and right subtrees
- If one subtree is deeper, return its LCA (the answer lies in that subtree)
- If both subtrees have equal depth, the current node is the LCA of all deepest nodes

### Algorithm

```
dfs(node):
    if node is null:
        return (0, None)

    left_depth, left_lca = dfs(node.left)
    right_depth, right_lca = dfs(node.right)

    if left_depth > right_depth:
        return (left_depth + 1, left_lca)
    elif right_depth > left_depth:
        return (right_depth + 1, right_lca)
    else:
        return (left_depth + 1, node)  # Current node is LCA
```

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of nodes in the tree
  - We visit each node exactly once during the DFS traversal

- **Space Complexity:** O(h) where h is the height of the tree
  - Space is used by the recursion call stack
  - In the worst case (skewed tree), h = n
  - In the best case (balanced tree), h = log(n)

## Key Insights

1. **Lowest Common Ancestor (LCA):** The smallest subtree containing all deepest nodes is rooted at the LCA of those nodes.

2. **Depth Comparison:** By comparing depths of left and right subtrees at each node, we can determine where the LCA is located:
   - If depths are equal, current node is the LCA
   - Otherwise, the LCA is in the deeper subtree

3. **Single Pass:** The solution elegantly combines depth calculation and LCA finding in a single DFS pass, avoiding the need for multiple traversals.

## Edge Cases

1. Single node tree → The node itself is the answer
2. All deepest nodes in left subtree → Return LCA from left subtree
3. All deepest nodes in right subtree → Return LCA from right subtree
4. Deepest nodes split between left and right → Current node is the LCA
