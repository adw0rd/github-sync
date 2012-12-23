#!/usr/bin/env python
"""github-sync: GitHub Repo Syncer

This script uses the GitHub API to get a list of all your repos in your GitHub account.
If the repo already exists locally, it will update it via git-pull.

Unlike https://github.com/kennethreitz/ghsync this package does not require a directory structure,
just point the way to the place where you have to find your repos. The default is "~".

This fork has roots from https://github.com/kennethreitz/ghsync/
I wanted to get my fork is simpler, without the directory structure, etc.
And just to recursively searched github-repository at the specified path and performed git-pull.
"""

__author__ = 'Mikhail Andreev'
__license__ = 'ISC'
__copyright__ = '2012 Mikhail Andreev'
__version__ = "0.1.1"

import os
import sys
import json

import requests
from clint import args
from clint.textui import puts, colored, indent
from github2.client import Github

try:
    # check_output is new in 2.7.
    from subprocess import check_output
    def cmd(command):
        return check_output(command, shell=True).strip()
except ImportError:
    # commands is deprecated and doesn't work on Windows
    from commands import getoutput as cmd

# GitHub configurations
GITHUB_USER = cmd('git config github.user')
GITHUB_TOKEN = cmd('git config github.token')
GITHUB_SYNC_DIR = os.environ.get('GITHUB_SYNC_DIR', '.')


def run():
    github = Github(username=GITHUB_USER, api_token=GITHUB_TOKEN)
    os.chdir(GITHUB_SYNC_DIR)
    repos = []
    for path_to_repo in cmd('find {0} -name ".git"'.format(GITHUB_SYNC_DIR)).split("\n"):
        # Receive repositories
        repos.append(path_to_repo[0:-4])
    for repo in repos:
        os.chdir(repo)
        try:
            # Receive current branch name
            branch = [br.split()[1] for br in cmd('git branch').split('\n') if br.split()[0] == "*"][0]
        except:
            puts(colored.yellow('Unkown branch in repository "{0}"!'.format(repo)))
        for remote in cmd('git remote -v').split('\n'):
            # Receive all remotes for repository
            remote = remote.split()
            if remote and remote[2] == "(fetch)" and 'github.com:' in remote[1]:
                puts(colored.green('Updating repo:'))
                puts(colored.cyan('> {0}'.format(repo)))
                puts(colored.cyan('> {0} ({1})'.format(remote[0], remote[1])))
                os.system('git pull {0} {1}'.format(remote[0], branch))

if __name__ == '__main__':
    run()

