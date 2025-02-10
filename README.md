# finals
# Custom File Processor

This repository demonstrates a custom file-processing project in Python that includes:

- **CustomFile**:
  - Reads file contents using a generator.
  - Uses a property (with getter/setter) to manage the file path.
  - Implements static and class methods.
  - Overloads `__str__` and `__add__` to output and concatenate file contents.
  - Provides methods to concatenate two files (using `__add__`) and to concatenate any number of files.

- **DecoratedFile**:
  - Inherits from `CustomFile`.
  - Overrides `__str__` to produce colored text output using a custom decorator.
  - Overrides `concat_with` to log the concatenation process.

- **Custom Decorator**:
  - `@colorize("red")` (or any other ANSI color) changes the text color of the function's output without using any external package.
## Setup Instructions

1. **Create Virtual Environment and Install Dependencies:**

   ```bash
   make venv
   make install
The code for the final assignment. (Mohamad Mahmoud, Adil Rehan, Given Pandala)
