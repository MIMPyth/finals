from final2 import *

if __name__ == "__main__":
    file_input = input("Enter file names to concatenate (comma-separated): ")
    file_list = [file.strip() for file in file_input.split(",")]

    color_choice = input("Enter a color for output text (red, green, yellow, blue, magenta, cyan, white): ").strip().lower()

    concat = FileConcatenator.from_file_list("output.txt", file_list, color=color_choice)

    print("\nConcatenation Complete!")
    print(concat.content)
    print("\nReading lines from concatenated file:")
    for line in concat.file_line_generator():
        print(line)