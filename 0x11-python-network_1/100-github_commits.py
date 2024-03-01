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
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    )

    response = requests.get(url)

    commit_list = response.json()
    try:
        for i in range(10):
            print(
                "{}: {}".format(
                    commit_list[i].get("sha"),
                    commit_list[i].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
