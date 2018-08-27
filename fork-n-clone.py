import gitlab
import os
import argparse
import time
from git import Repo


parser = argparse.ArgumentParser(description='Fork \'n clone Gitlab Repo')
parser.add_argument('-name',
                    type=str,
                    metavar='n',
                    help='repo to fork \'n clone',
                    required=True)

parser.add_argument('-teamname',
                    type=str,
                    metavar='t',
                    help='team repo is from',
                    required=True)
args = parser.parse_args()

gl_url = os.environ.get('gl_url')
gl_token = os.environ.get('gl_token')
gl = gitlab.Gitlab(gl_url, gl_token)

repo = gl.projects.get(args.teamname + '/' + args.name)

fork = repo.forks.create({})
timer.sleep(5)

Repo.clone_from(fork.ssh_url_to_repo, '~/git/' + args.name)

