import os

# Define the directory structure as a dictionary where keys are directories
# and values are lists of files (with optional initial content)
structure = {
    "config": {"config.yaml": "# Configuration settings\n"},
    "data": {"sample_data.csv": "id,value\n1,example\n"},
    "docs": {"architecture.md": "# Architecture Documentation\n\nDescribe your project architecture here.\n"},
    "notebooks": {"exploratory.ipynb": ""},  # Leave notebooks empty or add a basic JSON template if needed.
    "src": {
        "__init__.py": "",
        "app": {
            "__init__.py": "",
            "dashboard.py": "# Streamlit dashboard logic goes here\n",
            "components": {"__init__.py": ""},
        },
        "business": {"__init__.py": "", "model.py": "# Functions for business model calculations (CPA, LTV, etc.)\n"},
        "utils": {"__init__.py": "", "logger.py": "# Logging helper functions\n"},
        "config_loader.py": "# Code to load configuration settings\n",
    },
    "tests": {
        "__init__.py": "",
        "test_app.py": "# Tests for the app module\n",
        "test_business.py": "# Tests for the business logic\n",
        "test_utils.py": "# Tests for the utilities\n",
    },
}

# Files at the root of the project
root_files = {
    ".flake8": ("[flake8]\n" "max-line-length = 120\n" "extend-ignore = E203, W503\n"),
    "pyproject.toml": (
        "[tool.black]\n" "line-length = 120\n" "target-version = ['py39']\n\n" "[tool.isort]\n" 'profile = "black"\n'
    ),
    "requirements.txt": ("streamlit\n" "pytest\n" "black\n" "isort\n" "flake8\n"),
    "setup.py": ("# Setup script if you want to make your project installable\n"),
    "README.md": ("# Project Overview\n\n" "Description of the project.\n"),
}


def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # This is a directory. Create it.
            os.makedirs(path, exist_ok=True)
            # Recursively create its contents.
            create_structure(path, content)
        else:
            # This is a file. Create and write content.
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created file: {path}")


def create_root_files(base_path, files):
    for filename, content in files.items():
        file_path = os.path.join(base_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {file_path}")


if __name__ == "__main__":
    base_directory = os.getcwd()  # You can set this to a specific path if needed
    create_structure(base_directory, structure)
    create_root_files(base_directory, root_files)
    print("Project scaffolding complete!")
