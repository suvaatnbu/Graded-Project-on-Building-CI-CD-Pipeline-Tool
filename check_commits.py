import requests
import json
import os

# GitHub Repo Details
USER = 'suvaatnbu'  # Replace with your GitHub username
REPO = 'Graded-Project-on-Building-CI-CD-Pipeline-Tool'  # Replace with your repo name
API_URL = f'https://api.github.com/repos/{USER}/{REPO}/commits'

# Path to store the last commit hash
LAST_COMMIT_FILE = 'last_commit.txt'


def get_last_commit():
    """Reads the last stored commit hash from a file."""
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, 'r') as file:
            return file.read().strip()
    return None


def save_last_commit(commit_sha):
    """Saves the latest commit hash to a file."""
    with open(LAST_COMMIT_FILE, 'w') as file:
        file.write(commit_sha)


def check_for_new_commits():
    """Fetches the latest commits from the GitHub API and compares them."""
    print("Checking for new commits...")
    
    # Get the latest commits from GitHub API
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        commits = response.json()
        latest_commit_sha = commits[0]['sha']
        
        print(f"Latest commit SHA: {latest_commit_sha}")
        
        # Get the last checked commit SHA
        last_commit_sha = get_last_commit()
        
        if last_commit_sha == latest_commit_sha:
            print("No new commits.")
        else:
            print("New commits found!")
            # You can add code to do something when new commits are found
            save_last_commit(latest_commit_sha)
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        print(response.text)


if __name__ == '__main__':
    check_for_new_commits()

