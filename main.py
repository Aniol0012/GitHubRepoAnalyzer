import requests
import matplotlib.pyplot as plt
from datetime import datetime
import config
import gettext

gettext.bindtextdomain('messages', 'locale')
gettext.textdomain('messages')
lang_trans = gettext.translation('messages', localedir='locale', languages=[config.LANGUAGE], fallback=True)
lang_trans.install()
_ = lang_trans.gettext

token = config.TOKEN
repo = config.REPO
base_url = f"https://api.github.com/repos/{repo}"


def parse_repo(repo: str) -> str:
    return '/'.join(repo.rstrip('/').split('/')[-2:])


def get_commits() -> list[dict]:
    if config.MAX_COMMITS_TO_FETCH is None:
        commits_url = f"{base_url}/commits"
    else:
        commits_url = f"{base_url}/commits?per_page={config.MAX_COMMITS_TO_FETCH}"
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
        author_info = commit.get("author") or commit.get("commit", {}).get("author")
        if author_info and author_info.get("login"):
            username = author_info["login"]
        elif author_info and author_info.get("name"):
            username = author_info["name"]
        else:
            continue

        if username not in contributors:
            contributors[username] = {"commits": 0, "lines_added": 0}
        contributors[username]["commits"] += 1
        commit_details = get_commit_details(commit["url"])
        stats = commit_details.get("stats", {})
        contributors[username]["lines_added"] += stats.get("additions", 0)
    return contributors


def get_plots_count() -> int:
    return sum([config.SHOW_COMMITS_PLOT, config.SHOW_LINES_ADDED_PLOT])


def plot_data(contributors: dict) -> None:
    plots_count = get_plots_count()
    fig, ax = plt.subplots(plots_count, 1, figsize=(10, 8))

    if plots_count == 1:
        ax = [ax]

    generation_date = datetime.now().strftime("%Y-%m-%d")
    fig.suptitle(_("Report generated on: ") + generation_date, fontsize=12, x=0.95, ha="right")

    current_plot = 0

    if config.SHOW_COMMITS_PLOT:
        sorted_contributors = sorted(
            contributors.items(), key=lambda item: item[1]["commits"], reverse=True
        )
        if config.MAX_CONTRIBUTORS is not None:
            sorted_contributors = sorted_contributors[:config.MAX_CONTRIBUTORS]

        names = [f"{item[0]} \n[{item[1]['commits']}]" for item in sorted_contributors]
        commit_counts = [item[1]["commits"] for item in sorted_contributors]

        total_commits = sum(commit_counts)
        ax[current_plot].bar(
            names,
            commit_counts,
            color=config.COMMITS_BAR_COLOR,
        )
        ax[current_plot].set_title(_("Number of Commits per Contributor") +
                                   _(" (Total Commits: ") + str(total_commits) + ")")
        ax[current_plot].set_ylabel(_("Number of Commits"))
        current_plot += 1

    if config.SHOW_LINES_ADDED_PLOT:
        sorted_contributors = sorted(
            contributors.items(), key=lambda item: item[1]["lines_added"], reverse=True
        )
        if config.MAX_CONTRIBUTORS is not None:
            sorted_contributors = sorted_contributors[:config.MAX_CONTRIBUTORS]

        names = [f"{item[0]} \n[{item[1]['lines_added']}]" for item in sorted_contributors]
        lines_added = [item[1]["lines_added"] for item in sorted_contributors]

        total_lines_added = sum(lines_added)
        ax[current_plot].bar(
            names,
            lines_added,
            color=config.LINES_ADDED_BAR_COLOR,
        )
        ax[current_plot].set_title(_("Lines Added per Contributor") +
                                   _(" (Total Lines Added: ") + str(total_lines_added) + ")")
        ax[current_plot].set_ylabel(_("Number of Lines Added"))

    plt.tight_layout()
    plt.show()


def main() -> None:
    global repo, base_url
    repo = parse_repo(repo)
    base_url = f"https://api.github.com/repos/{repo}"
    commits = get_commits()
    contributors = analyze_commits(commits)
    plot_data(contributors)


if __name__ == "__main__":
    main()
