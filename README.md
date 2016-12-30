# jupyter-munin

A munin plugin to monitor the amount of Jupyter notebooks on your Linux sever.
 
## Introduction

   This python script is a [Munin](http://munin-monitoring.org) plugin for monitoring the [Jupyter](http://jupyter.org/) notebooks.

## Installation & Configuration 

0. Pre-requesites for the plugin is the [Requests](http://docs.python-requests.org/en/master/) library. To install it  
    
        $ pip install requests

1. Copy all the scripts to =/usr/share/munin/plugins
   
2. Create symbolic links to /etc/munin/plugins.

3. Restart the munin-node daemon: /etc/init.d/munin-node restart.

4. Done. You should now start to see the charts on the Munin pages.
