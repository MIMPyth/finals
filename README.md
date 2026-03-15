#  File Concatenator Project

This project is a **Python-based file concatenation utility** that reads multiple text files, merges their contents into a single output file, and displays the result with optional colored output in the terminal.

The project demonstrates several **object-oriented programming concepts in Python**, including:

- Classes and inheritance
- Class methods
- Static methods
- Operator overloading
- Generators
- Decorators
- File handling

---

#  Project Structure

```
finals-main/
│
├── main.py                # Main program that runs the file concatenation
├── final2.py              # Core classes and functionality
├── test_final2.py         # Unit tests
├── requirements.txt       # Python dependencies
├── text1.txt              # Example input file
├── text2.txt              # Example input file
├── output.txt             # Generated output file
│
├── .github/
│   └── workflows/
│       ├── main.yml
│       └── python-package-conda.yml
│
└── README.md
```

---

# ⚙️ Features

## File Concatenation
Multiple text files can be combined into a single output file.

Example:

```
text1.txt + text2.txt → output.txt
```

---

## Colored Terminal Output

The program supports colored output using ANSI escape codes.

Supported colors include:

- red
- green
- yellow
- blue
- magenta
- cyan
- white

Example output is displayed in the chosen color.

---

## Generator for Reading Lines

The program uses a **generator function** to read the output file line by line efficiently.

```python
for line in concat.file_line_generator():
    print(line)
```

---

## Logging Decorator

A decorator is used to log function execution.

Example:

```
Executing concatenate_files...
```

---

## Operator Overloading

Two `FileConcatenator` objects can be merged using the `+` operator.

Example:

```python
new_file = file1 + file2
```

This creates a new concatenated file containing both outputs.

---

#  How to Run

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/file-concatenator.git
```

---

## 2. Navigate into the folder

```bash
cd finals-main
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the program

```bash
python main.py
```

---

#  Example Output

```
Executing concatenate_files...

Concatenation Complete!
Concatenated 2 files into output.txt

Reading lines from concatenated file:
Hello from file 1
Hello from file 2
```

---

#  Running Tests

Unit tests are included to verify functionality.

Run tests using:

```bash
pytest
```

or

```bash
python test_final2.py
```

---

#  Concepts Demonstrated

This project demonstrates several Python programming techniques:

- Object-Oriented Programming (OOP)
- File Handling
- Decorators
- Generators
- Operator Overloading
- Unit Testing
- Continuous Integration (GitHub Actions)

---

#  Future Improvements

Possible improvements for the project:

- Command-line arguments for file input
- Support for more file formats
- GUI interface
- Better error handling
- File preview before concatenation

---

#  Author

The code for the final assignment. (Mohamad Mahmoud, Adil Rehan, Given Pandala)
