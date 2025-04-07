# File Read & Write Challenge 🖋️
try:
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    # Open the input file for reading
    with open(input_filename, "r") as input_file:
        content = input_file.readlines()

    # Modify the content (e.g., add line numbers)
    modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

    # Askgit  the user for the output filename
    output_filename = input("Enter the name of the file to write to: ")

    # Write the modified content to the output file
    with open(output_filename, "w") as output_file:
        output_file.writelines(modified_content)

    print(f"Modified content has been written to {output_filename}.")

# Error Handling Lab 🧪
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: The file could not be read or written.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")