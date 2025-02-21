import sys
from pathlib import Path

# Add the 'src' directory to sys.path so that pytest can find your packages.
sys.path.insert(0, str(Path(__file__).parent / "src"))
