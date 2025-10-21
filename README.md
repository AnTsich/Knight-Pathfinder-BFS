# Knight Pathfinder 

A Python program that finds the **shortest path a knight can take** on a standard chessboard from a given starting square to a destination square.
The algorithm is implemented using **Breadth-First Search (BFS)**, ensuring that the path found is always optimal.

---

# Algorithm Overview

The program uses the **BFS algorithm** to explore all possible knight moves on an 8×8 chessboard.
Each cell on the board is represented by a `Node` object that stores:

* Its position `(i, j)`
* Its distance from the starting point
* A reference to its parent node (used to reconstruct the path)

---

# How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AnTsich/knight-pathfinder-bfs.git
   cd knight-pathfinder
   ```

2. **Run the script**:

   ```bash
   python knight_pathfinder.py
   ```

3. **Enter the starting and destination squares** (0–7 range):

   ```
   Enter the starting square: 0 0
   Enter the destination square: 7 7
   ```

4. The program will print the **shortest path** in coordinate form.

---

# Example Output

```
Enter the starting square: 0 0
Enter the destination square: 7 7

(0, 0)
(1, 2)
(2, 4)
(3, 6)
(5, 7)
(7, 6)
(7, 7)
```

---

# Author

Created by @AnTsich
Mathematics student with an interest in algorithms, problem solving, and Python programming.
