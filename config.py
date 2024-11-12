from os import environ
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

TOKEN = environ.get("TOKEN")
REPO = environ.get("REPO")
LANGUAGE = environ.get("LANGUAGE", "en")

SHOW_COMMITS_PLOT = True
SHOW_LINES_ADDED_PLOT = True
MAX_CONTRIBUTORS = 7  # Set to None to show all contributors
MAX_COMMITS_TO_FETCH = None  # Set to None to fetch all commits

# Styles
COMMITS_BAR_COLOR = "steelblue"
LINES_ADDED_BAR_COLOR = "green"
