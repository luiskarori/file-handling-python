# File Read & Write + Error Handling Challenge

def main():
    try:
        # Ask user for input filename
        filename = input("Enter the name of the file to read: ")

        # Try opening the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (for example, make it uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        with open("modified_" + filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File modified successfully! Saved as modified_{filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
