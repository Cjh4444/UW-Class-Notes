import os
# Configuration
DIRECTORY = '/Users/camdencambre/UW Class Notes/notes'  # Change this to your target directory
PREFIX = 'Classes.'  # Change this to your desired prefix

# Function to rename files
def add_prefix_to_md_files(directory, prefix):
    try:
        # List all files in the directory
        for filename in os.listdir(directory):
            # Check if the file has a .md extension
            if filename.endswith('.md'):
                if filename.startswith('root') or filename.startswith('template'):
                    continue
                old_path = os.path.join(directory, filename)
                new_filename = prefix + filename
                new_path = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_filename}')

        print('Renaming completed!')

    except Exception as e:
        print(f'An error occurred: {e}')

# Execute the function
if __name__ == '__main__':
    add_prefix_to_md_files(DIRECTORY, PREFIX)
