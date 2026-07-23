# Task 7: Handle file-related errors using try and except (simple)

filename = "data.txt"

try:
    with open(filename, "r") as f:
        content = f.read()
        print("File content:\n", content)

except FileNotFoundError:
    print(f"Error: '{filename}' not found. Creating the file...")
    with open(filename, "w") as f:
        f.write("This is a new file.\n")
    print("File created successfully.")

except PermissionError:
    print(f"Error: Permission denied to access '{filename}'.")

except Exception as e:
    print("Unexpected error:", e)
