import github
import os

g = github.Github(os.environ.get('GITHUB_ACCESS_TOKEN'))

repos = g.get_user().get_repos()

for repo in repos:
    print(repo.name)
    print(repo.ssh_url + "\n")