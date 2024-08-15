import os
import subprocess
import unittest

class TestSort(unittest.TestCase):
    TMP_DIR = "test/tmp"
    
    # ======================================
    # Test Setup and Helpers
    # ======================================
    def runSort(input_arg) -> [str]:
        sort_py_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/sort.py"
        output_arg = TestSort.TMP_DIR + '/output.txt'
        result = subprocess.run(['python3', sort_py_path, input_arg, output_arg], capture_output=True, text=True)
        with open(output_arg, 'r') as file:
            return file.readlines()

    def write_file(output_filepath: str, list: [str]) -> None:
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, 'w') as file:
            file.writelines([l + '\n' for l in list])
    
    def cleanup():
        for filename in os.listdir(TestSort.TMP_DIR):
            file_path = os.path.join(TestSort.TMP_DIR, filename)
            
            # Check if it's a file and not a directory
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' has been removed.")
        os.rmdir(TestSort.TMP_DIR)

    def helper_test(self, expected, files: [[str]]):
        try:
            for i in range(len(files)):
                TestSort.write_file(TestSort.TMP_DIR + "/file" + str(i), files[i])

            actual = [l.strip() for l in TestSort.runSort(TestSort.TMP_DIR)]
            
            self.assertListEqual(expected, actual)
        finally:
            TestSort.cleanup()
    
    # ======================================
    # Test Cases
    # ======================================
    def testSimple(self):
        file1_lines = ['a', 'x', '\n', 'c', 'cc', '\n']
        file2_lines = ['z', 'x', '\n', 'b', 'c c']
        expected = ['a', 'b', 'c', 'c c', 'cc', 'x', 'x', 'z']
        self.helper_test(expected, [file1_lines, file2_lines])

    # Add more tests here

        


if __name__ == '__main__':
    unittest.main()