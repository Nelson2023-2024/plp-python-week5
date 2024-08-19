# file_handling_assignment.py

def file_handling_operations():
    try:
        # Step 1: File Creation and Writing
        with open("my_file.txt", "w") as file:
            file.write("Line 1: This is the first line.\n")
            file.write("Line 2: 12345 - Some numbers.\n")
            file.write("Line 3: Another line with text and numbers: 6789.\n")
        print("File created and initial content written successfully.")

        # Step 2: File Reading and Display
        with open("my_file.txt", "r") as file:
            print("\nReading and displaying the content of 'my_file.txt':")
            content = file.read()
            print(content)

        # Step 3: File Appending
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Adding more content.\n")
            file.write("Line 5: Appending some text.\n")
            file.write("Line 6: Final line of the file.\n")
        print("Additional lines appended successfully.")

        # Step 4: Read and display the file after appending
        with open("my_file.txt", "r") as file:
            print("\nReading and displaying the content of 'my_file.txt' after appending:")
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile handling operations completed.")

if __name__ == "__main__":
    file_handling_operations()
