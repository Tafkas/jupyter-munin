#!/usr/bin/env python
# encoding: utf-8
"""
juypter_notebooks_munin.py  A munin plugin for Linux to monitor the amount of jupyter notebooks
Copyright (C) 2016 Christian Stade-Schuldt
Author: Christian Stade-Schuldt
Like Munin, this plugin is licensed under the GNU GPL v2 license
http://www.opensource.org/licenses/GPL-2.0
"""
import sys

import requests

# This is the URL to your Jupyter Noteobook server's API endpoint
BASE_URL = 'http:<myserver>/api/{}'


def get_number_of_notebooks():
    """
    :return: the number of all notebooks hosted on the server including sub-directories
    """
    r = requests.get(BASE_URL.format('contents'))
    data = r.json()
    directories = []
    number_of_notebooks = 0

    # get notebooks and directories at the root
    for elem in data['content']:
        if elem['type'] == 'directory':
            directories.append(elem['path'])
        if elem['type'] == 'notebook':
            number_of_notebooks += 1

    # get nested notebooks and directories
    while len(directories) > 0:
        current_dir = directories.pop()
        r = requests.get(BASE_URL.format('contents') + '/{}'.format(current_dir))
        data = r.json()
        for elem in data['content']:
            if elem['type'] == 'directory':
                directories.append(elem['path'])
            if elem['type'] == 'notebook':
                number_of_notebooks += 1
    return number_of_notebooks


def get_number_of_running_notebooks():
    """
    :return:  the number of all currently running notebooks
    """
    r = requests.get(BASE_URL.format('sessions'))
    data = r.json()
    return len(data)


def print_config():
    print("graph_title Jupyter Notebooks")
    print("graph_args --base 1000")
    print("graph_vlabel Number of Jupyter Notebooks")
    print("graph_category jupyter")
    print("graph_order nb nba")
    print("nb.label no of notebooks")
    print("nb.type GAUGE")
    print("nb.draw AREA")
    print("nb.min 0")
    print("nb.info The number of all notebooks on the server")
    print("nba.label no of running notebooks")
    print("nba.type GAUGE")
    print("nba.draw AREA")
    print("nba.min 0")
    print("nba.info The number of currently running notebooks on the server")


def main():
    number_of_notebooks = get_number_of_notebooks()
    print('nb.value {}'.format(number_of_notebooks))
    number_of_running_notebooks = get_number_of_running_notebooks()
    print('nba.value {}'.format(number_of_running_notebooks))


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'config':
        print_config()
    elif len(sys.argv) == 2 and sys.argv[1] == 'autoconf':
        print('yes')
    elif len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == 'fetch':
        # Some docs say it'll be called with fetch, some say no arg at all
        try:
            main()
        except:
            sys.exit("Couldn't retrieve jupyter notebooks data")
