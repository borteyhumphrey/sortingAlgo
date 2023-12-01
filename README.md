
# Generator

Use genBookRecords.py script to generate the book records. To generate a book records of a specific number:
1. Open the terminal
2. Cd into folder containing script (in this case **project1c_completed**)
3. Type ```python3 genBookRecords.py 5000 > 5k.txt``` to generate 5000 book records and save as a file named "5k.txt" (filename and number can be changed as desired). To just print records in the terminal just type ```python3 genBookRecords.py 5000```

# Algorithms

The algorithms are named:
- linSearch.py (for linear search algorithm)
- binSearch.py (for binary search algrithm)
- mergeSort.py (for merge sort algorithm)

## Input files

The respective files are named with their input sizes(eg.5k.txt, 10k.txt, etc)

## Running the algorithms

- Still in the main folder in terminal (in this case **project1c_completed**)
- To run an alogrithm type: ```python3 linSearch.py``` and hit enter (for linear search. change as needed)
- When prompted, enter the file path for input data
    - Example: To use the 5000 input data just type 5k.txt (change as needed)

**NB:** Merge sort is already called in the Binary Search algorithm so there's no need to explicitly run merge sort before running binary search. If you wish to run merge sort follow the same procedure i.e., ```python3 mergeSort.py``` and enter name of input size to sort when prompted.


