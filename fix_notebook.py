import json

# Load the notebook
with open('notebooks/sprint3_model_experiments.ipynb', 'r') as f:
    nb = json.load(f)

# Find the cell with the error
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'source' in cell:
        source = ''.join(cell['source'])
        if '# Standardized residuals (true association strength)' in source:
            # Add import at the beginning
            cell['source'].insert(0, "import pandas as pd\n")
            break

# Save the notebook
with open('notebooks/sprint3_model_experiments.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)