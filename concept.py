Recursion
1. Recursivw function calls itself. Each recursive call reduce the size of problem. Recursion has to have base
 case (return's conditions) and a base case is reached. 

2. If fuction will not have base case we will get infinitive loop. Our function will go depper and depper and
    and never come back to start point.


Graph
Graphs is a tree (one item points to several items (>=0)) which can has a loop.
Tree can not have loops, graph can have loops.
Map of roads which connect cities in the state. Connections director and actors in movies (where they met)


Performance of Different Data Structures

Data ctructures                 Index   Search    Add-R    Add-L    Pop-L   Pop-R
Python List(Array)              O(1)    O(n)      O(1)     O(n)     O(n)    O(1)
Linked List                     O(n)    O(n)      O(1)     O(1)     O(1)    O(n)    
Doubly-Linked List              O(n)    O(n)      O(1)     O(1)     O(1)    O(1)
Queue(as Array)                 X       X         O(1)     X        O(n)    X
Queue (as LL or DLL)            X       X         O(1)     X        O(1)    X
Stack (as Array, LL, or DLL)    X       X         O(1)     X        X       O(1)
Dequeue(as DLL)                 X       X         O(1)     O(1)     O(1)    O(1)

Index: Find an item in the structure when you know a position
Search: Find an item in the strycture when you know its Data
Add(R/L): Set a key in set/dictionary or add node to treePop(R/L): Remove a key or node

Data Structures             Get         Add         Delete  Iterate     Memory
Dictionary(Hash Map)        O(1)        O(1)        O(1)    O(nLogn)    medium
Set(Hash Map)               O(1)        O(1)        O(1)    O(nLogn)    medium
Binary Search Tree          O(Logn)     O(Logn)     O(Logn) O(n)        small
Tree                        O(n)        O(n)        O(n)    O(n)        s

Get: Find an item in the structure
Add: Set a key in set/ditionary or add node to tree
Delete: Remove a key or node
Iterate: Find next iten in data structure
Memory: Relative to data, how much memory is used


Sorting
Buble sort:
Start from the begining, swap two elements if left element is greater than right. 
After all iteration the greatest number will be at the end.
Repeat steps excluding the item(s) at the end.

Merge Sort:
Recursevly divide a given list of numbers in two lists [:n] and [n:] (n - midpoint of current sublist) 
until these lists will contain 0 or 1 element. 
The list of one element is always sorted.
Combine by merging the two sorted subarrays back into the single sorted subarray. 

Quick Sort:
Choose a pivot.
Put numbers which are less or equal than the pivot to the left and numbers 
which are bigger than the pivot to the right of the pivot number. Concatinate two lists.
Recursevly repeat these steps for each new lists(less and greater) until each lists 
will contain only a pivot.
