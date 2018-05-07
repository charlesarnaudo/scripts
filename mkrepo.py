import github 
import os
import argparse

parser = argparse.ArgumentParser(description='Create GitHub Repo')
parser.add_argument('-name',
                    type=str,
                    metavar='',
                    help='name to give repo',
                    required=True)
parser.add_argument('-isPrivate',
                    type=bool,
                    metavar='',
                    help='Set repo to private or not',
                    required=False,
                    default=False)
args = parser.parse_args()

g = github.Github(os.environ.get('GITHUB_ACCESS_TOKEN'))

g.get_user().create_repo(name=args.name, private=args.isPrivate)