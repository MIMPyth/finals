from final2 import *

if __name__ == "__main__":
    file1 = "text1.txt" 
    file2 = "text2.txt"

    output_file = "output.txt"
    color_choice = "green"

    file_list = [file for file in [file1, file2] if os.path.exists(file)]
    
    if not file_list:
        print("this file does not exist. Check the file names.")
        exit()
    concat = FileConcatenator.from_file_list(output_file, file_list, color=color_choice)

    print("\nConcatenation Complete!")
    print(concat.content)
    print("\nReading lines from concatenated file:")
    for line in concat.file_line_generator():
        print(line)
