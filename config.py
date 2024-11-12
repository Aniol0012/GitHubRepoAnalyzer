from os import environ
from dotenv import load_dotenv
from enum import Enum


class SortBy(Enum):
    contribution = "contribution"
    name = "name"
    chronological = "chronological"

    def get_sort_key(self, contributor):
        if self == SortBy.contribution:
            return contributor[1]["commits"]
        if self == SortBy.name:
            return contributor[0].lower()
        if self == SortBy.chronological:
            return contributor[1]["commits"]


# This is the configuration file for the application

load_dotenv()

TOKEN = environ.get("TOKEN")
REPO = environ.get("REPO")
LANGUAGE = environ.get("LANGUAGE", "en")

SHOW_COMMITS_PLOT = True
SHOW_LINES_ADDED_PLOT = True
SORT_BY = SortBy.contribution
MAX_CONTRIBUTORS = 7  # Set to None to show all contributors
MAX_COMMITS_TO_FETCH = 100  # Set to None to fetch all commits

# Styles
COMMITS_BAR_COLOR = "steelblue"
LINES_ADDED_BAR_COLOR = "green"
