# This is the configuration file for the application

from os import environ

TOKEN = environ.get('TOKEN')
REPO = environ.get('REPO')

SHOW_COMMITS_PLOT = True
SHOW_LINES_ADDED_PLOT = True

## Styles
COMMITS_BAR_COLOR = 'steelblue'
LINES_ADDED_BAR_COLOR = 'green'