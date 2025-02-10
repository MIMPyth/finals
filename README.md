File Concatenation Program

Overview

This Python program concatenates multiple text files into a single output file while allowing users to apply colored text formatting. It provides an object-oriented approach with decorators, class methods, and operator overloading for enhanced functionality.

Features
Concatenates multiple text files into a single output file.
Supports ANSI color formatting for output text.
Implements a decorator for logging function execution.
Uses object-oriented programming principles with inheritance.
Includes operator overloading to allow concatenation of FileConcatenator objects.
Provides a generator method to yield colored lines from the output file.

Installation
Ensure you have Python installed on your system. No external dependencies are required.
Usage
Running the Program
Place the text files (text1.txt, text2.txt, etc.) in the same directory as the script.
Run the program using the command:
python main.py

How It Works
The program defines a BaseFileHandler class for handling file operations.
The FileConcatenator class extends BaseFileHandler and implements file concatenation logic.
The concatenate_files method reads and merges the content of multiple text files into a single output file.
The file_line_generator method prints the concatenated file content with the selected color.
The __add__ method enables merging two FileConcatenator instances into a new output file.

Code Structure

├── final2.py  # Contains the class definitions and file handling logic
├── main.py    # Main execution script
├── text1.txt  # Example input file
├── text2.txt  # Example input file
├── output.txt # Concatenated output file (generated after execution)
└── README.md  # Documentation

The code for the final assignment. (Mohamad Mahmoud, Adil Rehan, Given Pandala)
