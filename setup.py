import os
import sys
from distutils.core import setup

from github_sync import __version__

requirements = open('requirements.txt')
install_requires = []
dependency_links = []
try:
    for line in requirements.readlines():
        line = line.strip()
        if line and not line.startswith('#'):  # for inline  comments
            if "#egg" in line:
                names = re.findall('#egg=([^-]+)-', line)
                install_requires.append(names[0])
                dependency_links.append(line)
            else:
                install_requires.append(line)
finally:
    requirements.close()


setup(
    name='github-sync',
    version=__version__,
    description='Github Syncer. Checks and pulls all your GitHub repos',
    long_description=open('README.rst').read(),
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    license='ISC',
    url='https://github.com/adw0rd/github-sync',
    packages=['github_sync', ],
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'github-sync = github_sync:run',
        ],
    }
)
