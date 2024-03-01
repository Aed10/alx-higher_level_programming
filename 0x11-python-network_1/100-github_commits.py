#!/usr/bin/python3

"""
This script retrieves the latest 10 commits from a GitHub repository.

Usage:
    python3 100-github_commits.py <owner> <repo>

Arguments:
    <owner>: The owner of the GitHub repository.
    <repo>: The name of the GitHub repository.

Example:
    python3 100-github_commits.py octocat Hello-World

"""
import requests
import sys

if __name__ == "__main__":
    OWNER = sys.argv[2]
    REPO = sys.argv[1]
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        commit_list = response.json()[:10]
        for commit in commit_list:
            sha = commit["sha"]
            print(f"{sha}: {commit['commit']['author']['name']}")
