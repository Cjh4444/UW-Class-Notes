---
id: zp38zpipq3kf2n90ojypdzt
title: Lecture4
desc: ''
updated: 1736803301029
created: 1736800407406
---
# Topic: End of Asymptotic Analysis/Priority Queue ADT

## Todo:
- [ ] EX1 - Due Jan 17th

## Notes:
### Asymptotic Analysis
- Generally in 332 give O or Θ bound to worst-case of algorithm
- Cases
    - Best, **Worst**, Avg
- Bound
    - O - upper
    - Ω - lower
    - **Θ - tight**
### Priority Queue ADT
- Each item has a priority
- Min/Max heap underlying structure
- Operations
  - insert
  - deleteMin
      - returns and deletes item with highest priority
- Implementation Analysis

| Implementation        | Insert                                                 | deleteMin                              |
| --------------------- | ------------------------------------------------------ | -------------------------------------- |
| Unsorted Array        | O(1)                                                   | O(n)                                   |
| Unsorted Linked List  | O(1)                                                   | O(n)                                   |
| Sorted Circular Array | O(n)                                                   | O(1)                                   |
| Sorted Linked List    | O(n)                                                   | O(1)                                   |
| Binary Search Tree    | ~~O(log n)~~ O(n) (unbalanced BST, just a linked list) | ~~O(log n)~~ (BST could be unbalanced) |

### Trees
- Types of Trees
  - Binary
    - Every node has <2 nodes
  - N-ary
    - Every node have <n nodes
  - Perfect
    - Every row is completely full
  - Complete
    - All rows except bottom are full, and bottom row is filled left to right
  
### Min Heap
- Properties
  - Structure:
    - Complete (binary) tree
  - Heap Order Property
    - Every non-root node has a priority value larger than priority of parent
  - Operations
    - findMin
    - deleteMin: percolate (bubble) down
    - insert(val): percolate (bubble) up

    
    
