import os
import nbformat

# Get the folder where this script is located
folder_path = os.path.dirname(os.path.abspath(__file__))
print(f"Target folder: {folder_path}")

# Get the name of the script itself to exclude
this_script = os.path.basename(__file__)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    print(f"Checking file: {filename}")
    if filename.endswith('.md') and filename != this_script:
        print(f"Processing: {filename}")
        base_name = os.path.splitext(filename)[0]
        ipynb_name = base_name + '.ipynb'
        ipynb_path = os.path.join(folder_path, ipynb_name)

        # Create an empty Jupyter notebook
        nb = nbformat.v4.new_notebook()
        with open(ipynb_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)

        print(f"Created: {ipynb_name}")
    else:
        print(f"Skipped: {filename}")
