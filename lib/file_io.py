def write_file(file_name, file_content):
    """Writes content to a file with .txt extension."""
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Appends content to a file with .txt extension."""
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    """Reads and returns content from a file with .txt extension."""
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
