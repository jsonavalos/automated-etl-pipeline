import papermill as pm
import os
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)

# Get absolute project root
project_root = os.path.dirname(os.path.abspath(__file__))

notebooks_to_run = [
    'etl/extraction/extraction.ipynb',
    'etl/transformation/transformation.ipynb',
    'etl/loading/loading.ipynb'
]

output_dir = 'executed_notebooks'
os.makedirs(output_dir, exist_ok=True)

print(f"Project root: {project_root}\n")

for notebook in notebooks_to_run:
    output_name = os.path.basename(notebook).replace('.ipynb', '_executed.ipynb')
    output_path = os.path.join(output_dir, output_name)
    
    # Get the notebook's directory for cwd
    notebook_dir = os.path.join(project_root, os.path.dirname(notebook))
    
    print(f'Executing: {notebook}')
    print(f'Working directory: {notebook_dir}')
    
    try:
        pm.execute_notebook(
            input_path=os.path.join(project_root, notebook),
            output_path=output_path,
            cwd=notebook_dir 
        )
        print(f'✓ Success\n')
    except Exception as e:
        print(f"✗ Error: {e}\n")
        break