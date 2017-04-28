#! /usr/bin/env python3
# scripts for collecting filesystem data

import os
import subprocess

# gather info through bash

# check filesystem space
def get_df_hT():
    df_hT = str(subprocess.check_output(['df', '-hT']))
    df_hT = df_hT[:2]


# check for deleted files
lsof = subprocess.Popen(('lsof'), stdout=subprocess.PIPE)
grep_deleted = subprocess.check_output(['grep', 'deleted'], stdin=lsof.stdout)
# check filesystem usage
du_sh = subprocess.check_output(['du', '-sh'])
