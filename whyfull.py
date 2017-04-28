#! /usr/bin/env python3

import sys
import os

args = sys.argv

# TODO: show deleted files (lsof)
# TODO: show sparse files

# does what it says on the tin
def convert_string_to_float_to_int(num_string):
    if type(num_string) == str:
        try:
            return int(float((num_string)))
        except ValueError:
            print('CONVERSION ERROR')

# convert strings of format "42.5K" to actual byte size
def calculate_true_file_size(size):
    true_size = 0
    # this should succeed if the size is below 1K, since ls will not print any letters (e.g. K, M, G)
    try:
        true_size = convert_string_to_float_to_int(size)
        print(true_size)
        return true_size
    except ValueError:
        if 'K' in size:
            # take off the K
            true_size = size[:len(size)-1]
            print(true_size)
            # convert to bytes
            true_size = convert_string_to_float_to_int(true_size) * 1000

if len(args) != 2:
    print('Usage: whyful.py <file>')
else:
    file_name = args[1]
    file = open(file_name)
    print(file)
    for line in file:
        # split so we only see the file size and file name
        space_split = line.split(' ')
        # TODO: make this error checking more precise
        if len(space_split) >= 5:
            file_size = space_split[0]
            file_name = space_split[len(space_split)-1]
            print(file_size + ' ' + file_name)
