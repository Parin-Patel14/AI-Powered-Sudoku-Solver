#  Installation Guide  

This guide provides step-by-step instructions to set up the **AI-Powered Sudoku Solver** on your local machine.  

---

### **Option 1

##  Step 1: Clone the Repository  
First, download the project from GitHub by cloning the repository:  

```bash
git clone https://github.com/YOUR_USERNAME/AI-Powered-Sudoku-Solver.git
cd AI-Powered-Sudoku-Solver
```

---

### **Option 2: Download Files for each Algorithm**  

##  Step 1: Manual Downlaod 

1. **Manually download** the required files from the repository.  
2. **Create a new folder** on your system and place all downloaded files of a specific algorithm inside it.
3. **Open a terminal in that folder** to run the project.

---

##  Step 2: Set Up a Virtual Environment (Optional but Recommended)  
To avoid dependency conflicts, create and activate a virtual environment:  

```bash
# Create a virtual environment (for Windows)
python -m venv venv
venv\Scripts\activate

# Create a virtual environment (for macOS/Linux)
python3 -m venv venv
source venv/bin/activate
```
Note: A virtual environment is optional but highly recommended to isolate project dependencies.

---

##  Step 3: Install Required Dependencies  
Once inside the project folder, install the necessary Python libraries using `pip`:  

```bash
pip install pygame numpy
```
Dependencies Installed:

- Pygame → Used for GUI visualization of the Sudoku solver.
- NumPy → Used for array manipulations in puzzle-solving.
