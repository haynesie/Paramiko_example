#! /usr/bin/env python
#
#  (C) 2014 Keven Haynes

"""
   A simple example use case for Paramiko(ssh). This program checks the
   uptime of machines in a lab whose names are labelled by rows [1-8]
   and columns [a-h].  A list of machines that could not be be reached
   is printed to stdout. (It is best if you have ssh keys/agent set up for 
   password-less login.)

"""

import paramiko
import sys, os


def clusterNodeLoad():
    cmd = "/usr/bin/uptime"
    username = os.environ.get('USERNAME') or 'add_your_username'
    down_systems = []
    for i in range(1,9):
        for j in ('a','b','c','d','e','f','g','h'):
            host = "lab" + str(i) + j
            time = ""
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(host, username) 
                stdin, stdout, stderr = ssh.exec_command(cmd)
                time = stdout.readlines()[0].strip()
                if time: 
                    print '%s:  %s' % (host, time)
                ssh.close()
            except:
                print "Trouble with ", host,
                down_systems.append(host)

    if len(down_systems): 
        print "\nCheck on:  ",
        for node in down_systems:
            print node, 

if __name__ == '__main__':
    clusterNodeLoad()
