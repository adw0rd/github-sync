github-sync: GitHub Repo Syncer
================================

This script uses the GitHub API to get a list of all your repos in your GitHub account. If the repo already exists locally, it will update it via git-pull.

Unlike https://github.com/kennethreitz/ghsync this package does not require a directory structure, just point the way to the place where you have to find your repos. The default is "." (current directory), set the correct path::

    export GITHUB_SYNC_DIR='/path/to/repos'


Install
-------

To install github-sync, simply run::

    $ pip install github-sync
    ... or develop. version:
    $ pip install -e git://github.com/adw0rd/github-sync.git#egg=github-sync

The command ``github-sync`` will then be available to you from the command line.
::

    $ github-sync


History
--------

This fork has roots from https://github.com/kennethreitz/ghsync/

I wanted to get my fork is simpler, without the directory structure, etc.
And just to recursively searched github-repository at the specified path and performed git-pull
