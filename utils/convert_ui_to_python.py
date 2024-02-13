import subprocess
import sys

def generate_ui_code(ui_file, output_file):
    """
    Generate Python code from a .ui file using PySide6's pyside6-uic.exe.
    
    Args:
    - ui_file (str): Path to the .ui file.
    - output_file (str): Path to the output Python file.
    """
    # Path to pyside6-uic.exe
    pyside_uic = r"C:\Users\dominika\anaconda3\envs\innvestigate\Scripts\pyside6-uic.exe"
    
    # Command to execute
    command = [pyside_uic, ui_file, "-o", output_file]
    
    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Python code generated successfully from {ui_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        
# Example usage:
if __name__ == "__main__":
    # Check if the number of arguments provided is correct
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_ui_file.ui output_python_file.py")
        sys.exit(1)
    
    # Get the input .ui file and the output Python file from command-line arguments
    ui_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Generate the Python code from the .ui file
    generate_ui_code(ui_file, output_file)