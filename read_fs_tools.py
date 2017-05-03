#! /usr/bin/env python3
# scripts for collecting filesystem data

import os
import subprocess
import re

# gather info through bash

'''
b'Filesystem                Type      Size  Used Avail Use% Mounted on\n/dev/mapper/RHEL7CSB-Root ext4       29G   26G  1.7G  94% /\ndevtmpfs                  devtmpfs  7.6G
0  7.6G   0% /dev\ntmpfs                     tmpfs     7.6G  393M  7.2G   6% /dev/shm\ntmpfs                     tmpfs     7.6G  1.2M  7.6G   1% /run\ntmpfs                     tmpfs
    7.6G     0  7.6G   0% /sys/fs/cgroup\n/dev/sda1                 ext4      2.9G  241M  2.5G   9% /boot\n/dev/map
    per/RHEL7CSB-Home ext4       99G   77G   17G  83% /home\ntmpfs                     tmpfs     1.6G   40K  1.6G   1% /run/user/110451\n'
'''

'''
Filesystem                Type      Size  Used Avail Use% Mounted on
/dev/mapper/RHEL7CSB-Root ext4       29G   26G  1.7G  94% /
devtmpfs                  devtmpfs  7.6G     0  7.6G   0% /dev
tmpfs                     tmpfs     7.6G  393M  7.2G   6% /dev/shm
tmpfs                     tmpfs     7.6G  1.2M  7.6G   1% /run
tmpfs                     tmpfs     7.6G     0  7.6G   0% /sys/fs/cgroup
/dev/sda1                 ext4      2.9G  241M  2.5G   9% /boot
/dev/mapper/RHEL7CSB-Home ext4       99G   77G   17G  83% /home
tmpfs                     tmpfs     1.6G   44K  1.6G   1% /run/user/110451
'''

# placeholder for real df parsing function
def print_colored_output(string):
    split_string = string[2:].split('\n')
    # we want to find which column 'Avail' is in case that changes in other versions of df
    avail_column = ''
    for i in list(enumerate(split_string[0])):
        if i is 'Avail':
            avail_column = i[1]
    for line in split_string:

    print(list(enumerate(split_string)))

# check filesystem space
def get_df_hT():
    df_hT = str(subprocess.check_output(['df', '-hT']))
    df_hT = df_hT[:2]

'''
# check for deleted files
lsof = subprocess.Popen(('lsof'), stdout=subprocess.PIPE)
grep_deleted = subprocess.check_output(['grep', 'deleted'], stdin=lsof.stdout)
# check filesystem usage
du_sh = subprocess.check_output(['du', '-sh'])
'''
