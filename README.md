# Co-existence-Problem-Solver-Python-
This Python project solves the "co-existence problem" by efficiently processing text files and finding lines where all queried words appear together. It uses dictionaries and sets to map words to line numbers, ensuring fast lookups and optimal performance. The solution is designed to handle large text files, such as *War and Peace*, and includes functions for file handling, text preprocessing, and query-based searches.

Features:
- File Handling: Prompts the user to enter a filename and handles errors with a `try-except` loop.
- Text Preprocessing: Converts text to lowercase, removes punctuation, filters out non-alphabetic words, and handles hyphenated words.
- Efficient Word Mapping: Builds a dictionary where each word is mapped to the set of line numbers where it appears.
- Co-existence Query: Users can input space-separated query words to find lines where all the words coexist.
- Interactive Mode: Continuously prompts for new queries until `q` or `Q` is entered to quit.

Functions:
- `open_file()`: Prompts the user for a filename and opens the file with error handling.
- `read_file(fp)`: Reads and preprocesses the text, storing word-line mappings in a dictionary.
- `find_coexistence(D, query)`: Performs set intersection to find line numbers containing all queried words.

Helper Functions (Suggested):
- `remove_punctuation(words)`
- `process_lines(ls)`
- `is_word(word)`

Example Usage:
Given a text file with the following lines:
1. Try not to become a man of success, but rather try to become a man of value.  
2. Look deep into nature, and then you will understand everything better.  
3. The true sign of intelligence is not knowledge but imagination.  

If the query is:
Enter query: true knowledge imagination  

The program will output:
Lines: [3]  

Installation and Usage:
1. Clone the repository:
   git clone https://github.com/yourusername/coexistence-problem-solver.git  
   cd coexistence-problem-solver  
2. Ensure you have Python installed.
3. Run the program:
   python a6_part1_xxxxxx.py  
4. Follow the prompts to input filenames and query words.

Test Files:
The project includes sample test files (`einstein.txt`, `gettysburg.txt`) and instructions for testing with the *War and Peace* text file.

License:
This project is open-source and available under the MIT License.

Author:
Mohammadjavad Aghaeipour Kalyani – First-year Software Engineering Student at the University of Ottawa.
"""
