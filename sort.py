import heapq
import os
import sys

def read_and_sort_filelines(filepaths: str) -> [str]:
    # Heapsort

    # Push all lines into heap
    heap = []
    for path in filepaths:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    heapq.heappush(heap, line)
    sorted_lines = []

    # pop all out into sorted list
    while heap:
        sorted_lines.append(heapq.heappop(heap))
    return sorted_lines

def write_result(output_filepath: str, sorted_list: [str]) -> None:
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, 'w') as file:
        for i in range(len(sorted_list)):
            line = sorted_list[i]

            # Do not end file in new line
            if i < len(sorted_list) - 1:
                line += "\n"
            file.write(line)

def get_filepaths(directory: str) -> [str]:
    all_filepaths = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            all_filepaths.append(filepath)
    return all_filepaths

def main():
    input_directory = sys.argv[1]
    output_filepath = sys.argv[2]

    all_filepaths = get_filepaths(input_directory)
    sorted_lines = read_and_sort_filelines(all_filepaths)
    write_result(output_filepath, sorted_lines)

if __name__ == "__main__":
    main()