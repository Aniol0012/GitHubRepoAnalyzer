import requests
import matplotlib.pyplot as plt
import config

token = config.TOKEN
repo = config.REPO
base_url = f'https://api.github.com/repos/{repo}'

def get_commits():
    commits_url = f'{base_url}/commits'
    headers = {'Authorization': f'token {token}'}
    commits = []
    while commits_url:
        response = requests.get(commits_url, headers=headers)
        commits.extend(response.json())
        if 'next' in response.links:
            commits_url = response.links['next']['url']
        else:
            break
    return commits

def analyze_commits(commits):
    contributors = {}
    for commit in commits:

        if commit.get('author') and commit['author'].get('login'):
            username = commit['author']['login']
            if username not in contributors:
                contributors[username] = {'commits': 0, 'lines_added': 0}
            contributors[username]['commits'] += 1
            contributors[username]['lines_added'] += 10
    return contributors

def plot_data(contributors):
    names = [f"{name} [{contributors[name]['commits']}]" for name in contributors]
    commit_counts = [contrib['commits'] for contrib in contributors.values()]
    lines_added = [contrib['lines_added'] for contrib in contributors.values()]
    
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    
    if config.SHOW_COMMITS_PLOT:
        ax[0].bar(names, commit_counts, color=config.COMMITS_BAR_COLOR)
        ax[0].set_title('Number of Commits per Contributor')
        ax[0].set_ylabel('Number of Commits')
    
    if config.SHOW_LINES_ADDED_PLOT:
        ax[1].bar(names, lines_added, color=config.LINES_ADDED_BAR_COLOR)
        ax[1].set_title('Lines Added per Contributor')
        ax[1].set_ylabel('Number of Lines Added')
    
    plt.tight_layout()
    plt.show()

def main():
    commits = get_commits()
    contributors = analyze_commits(commits)
    plot_data(contributors)

if __name__ == '__main__':
    main()