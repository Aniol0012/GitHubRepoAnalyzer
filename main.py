import requests
import matplotlib.pyplot as plt
import config

token = config.TOKEN
repo = config.REPO
base_url = f"https://api.github.com/repos/{repo}"


def get_commits() -> list[dict]:
    commits_url = f"{base_url}/commits"
    headers = {"Authorization": f"token {token}"}
    commits = []
    while commits_url:
        response = requests.get(commits_url, headers=headers)
        commits.extend(response.json())
        if "next" in response.links:
            commits_url = response.links["next"]["url"]
        else:
            break
    return commits


def get_commit_details(commit_url: str) -> dict:
    headers = {"Authorization": f"token {token}"}
    response = requests.get(commit_url, headers=headers)
    return response.json()


def analyze_commits(commits: list) -> dict:
    contributors = {}
    for commit in commits:

        if commit.get("author") and commit["author"].get("login"):
            username = commit["author"]["login"]
            if username not in contributors:
                contributors[username] = {"commits": 0, "lines_added": 0}
            contributors[username]["commits"] += 1

            commit_details = get_commit_details(commit["url"])
            stats = commit_details.get("stats", {})
            contributors[username]["lines_added"] += stats.get("additions", 0)
    return contributors


def get_names(contributors: dict, type: str | None) -> list[str]:
    if not type:
        return [name for name in contributors]
    return [f"{name} [{contributors[name][type]}]" for name in contributors]


def get_plots_count() -> int:
    return sum([config.SHOW_COMMITS_PLOT, config.SHOW_LINES_ADDED_PLOT])


def plot_data(contributors: dict) -> None:
    commit_counts = [contrib["commits"] for contrib in contributors.values()]
    lines_added = [contrib["lines_added"] for contrib in contributors.values()]

    plots_count = get_plots_count()
    fig, ax = plt.subplots(plots_count, 1, figsize=(10, 8))

    if plots_count == 1:
        ax = [ax]

    current_plot = 0

    if config.SHOW_COMMITS_PLOT:
        ax[current_plot].bar(
            get_names(contributors, "commits"),
            commit_counts,
            color=config.COMMITS_BAR_COLOR,
        )
        ax[current_plot].set_title("Number of Commits per Contributor")
        ax[current_plot].set_ylabel("Number of Commits")
        current_plot += 1

    if config.SHOW_LINES_ADDED_PLOT:
        ax[current_plot].bar(
            get_names(contributors, "lines_added"),
            lines_added,
            color=config.LINES_ADDED_BAR_COLOR,
        )
        ax[current_plot].set_title("Lines Added per Contributor")
        ax[current_plot].set_ylabel("Number of Lines Added")

    plt.tight_layout()
    plt.show()


def main() -> None:
    commits = get_commits()
    contributors = analyze_commits(commits)
    plot_data(contributors)


if __name__ == "__main__":
    main()
