import os

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

class BaseFileHandler:
    def __init__(self, filename, color="white"):
        self.filename = filename
        self.color = self.validate_color(color)

    def __str__(self):
        return f"BaseFileHandler for {self.filename}"

    def __len__(self):
        return os.path.getsize(self.filename) if os.path.exists(self.filename) else 0

    @staticmethod
    def is_text_file(filename):
        return filename.endswith(".txt")

    @staticmethod
    def validate_color(color):
        colors = {
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "reset": "\033[0m"
        }
        return colors.get(color.lower(), colors["white"])
class FileConcatenator(BaseFileHandler):
    def __init__(self, filename, color="white"):
        super().__init__(filename, color)
        self._content = "" 

    @classmethod
    def from_file_list(cls, output_file, file_list, color="white"):
        instance = cls(output_file, color)
        instance.concatenate_files(file_list)
        return instance

    @log_execution
    def concatenate_files(self, file_list):
        with open(self.filename, "w") as outfile:
            for file in file_list:
                if os.path.exists(file):
                    with open(file, "r") as infile:
                        data = infile.read()
                        outfile.write(data + "\n")
            self.content = f"Concatenated {len(file_list)} files into {self.filename}"

    def file_line_generator(self):
        with open(self.filename, "r") as f:
            for line in f:
                yield f"{self.color}{line.strip()}\033[0m" 
    def __add__(self, other):
        if isinstance(other, FileConcatenator):
            new_filename = f"merged_{self.filename}_{other.filename}.txt"
            new_files = [self.filename, other.filename]
            return FileConcatenator.from_file_list(new_filename, new_files, self.color)
        raise TypeError("it cant be done")
