# jupyter-munin

A munin plugin to monitor the amount of Jupyter notebooks on your Linux sever.

## Introduction

   This python script is a [Munin](http://munin-monitoring.org) plugin for monitoring the [Jupyter](http://jupyter.org/) notebooks.

## jupyter-munin
jupyter-munin shows you the amount of Jupyter notebooks and the number of running Jupyter notebooks on your server
![http://i.imgur.com/TzbLrKy.png](http://i.imgur.com/TzbLrKy.png)

## Installation & Configuration

0. Pre-requesites for the plugin is the [Requests](http://docs.python-requests.org/en/master/) library. To install it  

        $ pip install requests

1. Copy all the scripts to /usr/share/munin/plugins.

2. Create symbolic links to /etc/munin/plugins.

3. Create entry in /etc/munin/plugin-conf.d/munin-node:

        [jupyter_*]  
        env.jupyter_url <url_to_your_jupyter_api_endpoint>  

4. Restart the munin-node daemon: /etc/init.d/munin-node restart.

5. Done. You should now start to see the charts on the Munin pages.
