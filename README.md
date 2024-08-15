# Explanation
Simple python CLI. Uses simple libraries like `os`, `heapq`, `sys`.

I know there's a lot more needed to be productionized, such as a cleaner wrapper, input validation, `-h` help hints, more tests, etc

File by file, reads line by line, pushing each line into a heap (if not empty).

Once all collected, pops it back into a sorted list, and writes to file


For testing, used `unittest` library.

# Instructions
Requires python to be installed

To run, run `python3 sort.py <input_dir> <output_path>` in the command line.
```
# example
python3 sort.py inputs output.txt
```

To test, run `python2 test/test_sort.py`. Tests are easily added (see `Test Cases` in test_sort.py)

# Analysis

Runtime complexity: O(nlogn), where n is total number of lines. We add `n` lines to the heapq. Each heappush is logn worst case, therefore overall complexity is n * log n.

Other considerations:
- limitation: all non-empty lines will be stored in memory, so memory may be a bottleneck for large number of total lines. 
- Can use mergesort instead, keeping the sorted sub-arrays on disk. This way, we only need to keep 1 line from each sub-array in memory. Performance may take a hit from i/o operations