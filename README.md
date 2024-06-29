# GitHub Repository Analyzer
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django?style=plastic)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
![GitHub issues](https://img.shields.io/github/issues/Aniol0012/GitHubRepoAnalyzer?style=plastic&color=yellow)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Aniol0012/GitHubRepoAnalyzer?style=plastic&color=pink)


This project analyzes the commits of a GitHub repository and visualizes the activity of contributors in terms of the number of commits and lines added. It uses the [GitHub API](https://docs.github.com/en/rest) to fetch repository data and generates charts for better understanding of the activity.

## Features

- Fetches commits from a GitHub repository.
- Analyzes contributors and their respective activities.
- Generates charts showing the number of commits and lines added by each contributor.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Computer-Engineering-UdL/JointProject.git
    cd JointProject
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:

    - Create a `.env` file in the root directory with the following command:
        ```bash
        touch .env
        ```
    - Then, define the following variables inside the file:
        ```bash
        GITHUB_TOKEN=your_github_token_here
        REPO=username/repo_name
        ```

> [!NOTE]
> You can generate a GitHub token by following the instructions [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

5. Configure visualization settings (optional):

    - You can customize the appearance of the charts by modifying the [`config.py`](config.py) file.

## Usage

Run the script to fetch commits and generate charts:

```bash
python main.py
```


## Customization

You can customize various aspects of the analysis and visualization in the `config.py` file:

- `SHOW_COMMITS_PLOT`: Show or hide the commits chart (True/False).
- `SHOW_LINES_ADDED_PLOT`: Show or hide the lines added chart (True/False).
- `COMMITS_BAR_COLOR`: Color of the bars in the commits chart.
- `LINES_ADDED_BAR_COLOR`: Color of the bars in the lines added chart.

## Contributing

Contributions are welcome. Please follow these steps to contribute:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'feat: add new feature'`).
4. Push your changes (`git push origin feature/new-feature`).
5. Open a Pull Request.

> [!NOTE]
> This project uses the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.


## License
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?)](https://opensource.org/license/mit/)


This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.


