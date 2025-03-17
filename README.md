#  AI-Powered Sudoku Solver  

 **An AI-based Sudoku solver that implements and benchmarks multiple search algorithms (BFS, DFS, IDS, CSP) for efficiency, accuracy, and scalability.** This project includes a **graphical user interface (GUI)** using Pygame to visualize the solving process and an automated performance evaluation system.

---

##  Overview  
The project aims to **evaluate the efficiency of different AI search algorithms** in solving Sudoku puzzles. Each algorithm is tested based on **execution time, recursive calls, and scalability** across different puzzle complexities.  

**Implemented Algorithms:**  
✅ **Depth-First Search (DFS)** – Classic backtracking approach  
✅ **Iterative Deepening Search (IDS)** – Hybrid DFS + BFS method  
✅ **Constraint Satisfaction Problem (CSP)** – Constraint-based backtracking  
✅ **Breadth-First Search (BFS)** – Level-wise exploration  

🔹 **Performance Metrics Analyzed:**  
- **Total Recursive Calls:** Measures algorithm efficiency.  
- **Execution Time:** Time taken to solve puzzles (in seconds).  
- **State Space Growth:** Tracks memory usage and computational complexity.  

---

##  Key Features  
 **AI-Based Sudoku Solving** – Uses BFS, DFS, IDS, and CSP for different solving strategies.  
 **Performance Benchmarking** – Tracks execution time & recursive calls for each approach.  
 **Pygame GUI** – Interactive Sudoku board visualization.  
 **Automated Testing** – Performance evaluation across multiple test cases.  

---

## 📊 Performance Analysis  

### **🔹 Algorithm Comparison**
| Algorithm | Avg Recursive Calls | Execution Time (Seconds) | Strengths | Weaknesses |
|-----------|--------------------|--------------------------|------------|-------------|
| **BFS** | 1,260 - 13,123 | **0.01 - 0.14** | Fastest for simple puzzles | High memory usage |
| **CSP** | **57 - 1882** | **6.81 - 379.28** | Best for complex puzzles | Slower than BFS for easy cases |
| **IDS** | 233 - 1466 | **3.08 - 145.97** | Optimized DFS alternative | Costly due to redundant depth iterations |
| **DFS** | 58 - 1702 | **7.68 - 341.36** | Simple & guaranteed solution | Slowest for complex puzzles |

 **Key Takeaways:**  
- ✅ **BFS is the fastest**, solving puzzles in **milliseconds** but uses **high memory**.  
- ✅ **CSP is optimal** for **harder puzzles**, minimizing recursion and invalid searches.  
- ⚠️ **DFS is the slowest**, requiring **deep recursion** and more processing time.  
- ⚠️ **IDS improves DFS performance** but is still not as optimized as CSP.  

---

## 🚀 Installation, Execution & Performance Benchmarking  

For detailed setup and usage, check:  
📌 **[Installation Guide](INSTALLATION.md)** – Steps to install dependencies.  
📌 **[Usage Instructions](USAGE.md)** – How to run the Sudoku solver.  
📌 **[Performance Benchmarking](PERFORMANCE.md)** – Evaluate algorithm efficiency.  

---

Follow these guides for proper setup and execution. Let me know if you face any issues! 🚀😊

