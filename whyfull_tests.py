#! /usr/bin/env python3

import pytest
import whyfull
import read_fs_tools

# what our actual output is currently from get_df_hT()
test_output = '''
b'Filesystem                Type      Size  Used Avail Use% Mounted on\n/dev/mapper/RHEL7CSB-Root ext4       29G   26G  1.7G  94% /\ndevtmpfs                  devtmpfs  7.6G
0  7.6G   0% /dev\ntmpfs                     tmpfs     7.6G  393M  7.2G   6% /dev/shm\ntmpfs                     tmpfs     7.6G  1.2M  7.6G   1% /run\ntmpfs                     tmpfs
    7.6G     0  7.6G   0% /sys/fs/cgroup\n/dev/sda1                 ext4      2.9G  241M  2.5G   9% /boot\n/dev/map
    per/RHEL7CSB-Home ext4       99G   77G   17G  83% /home\ntmpfs                     tmpfs     1.6G   40K  1.6G   1% /run/user/110451\n'
'''

expected_output = '''
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

def test_print_colored_output():
    assert read_fs_tools.print_colored_output(test_output) == expected_output
    
