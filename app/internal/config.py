from pathlib import Path

# Path to the root of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# static files root directory
STATIC_DIR = BASE_DIR / 'static'

# Templates root directory
TEMPLATE_DIR = BASE_DIR / 'templates'