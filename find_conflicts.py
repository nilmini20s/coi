#!/usr/bin/python

import sys
import re


institutions = set(['AMD', 
    'ARM', 
    'Apple', 
    'Google'
    'HP',
    'IBM',
    'LLNL',
    'MediaTek',
    'Michigan',
    'Microsoft', 
    'NVIDIA',
    'ORNL',
    'Penn',
    'Illinois',
    'Intel', 
    'Qualcomm',
    'Stanford',
    'Toronto'])

stray_words = set(['Labs',
    'Inc',
    'Research',
    'State',
    'Tech'])

############################
### Function Definitions ###
############################

def usage():
    print "================================================================="
    print "===========  Script for finding conflicts of interest  =========="
    print "Usage:./find_coflicts.py <your_list.txt> <program_committee.txt>"
    print "Each file should have one name per line. Commas and paranthesis are fine."
    print "================================================================="
# end usage

def setOfNames(filename):
    f = open(filename, 'r')
    list_of_names = []
    for line in f:
        line = line.translate(None,'(),')
        name = line.split()
        list_of_names.extend(name)

    set_of_names = set(list_of_names)
    return set_of_names
# end setOfNames

############################
### Main Program         ###
############################

if (len(sys.argv) < 3):
    usage()
    exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

names1 = setOfNames(file1)
names2 = setOfNames(file2)

# Find common words in both sets
common = names1.intersection(names2)

# Take out any not-important stray words
common = common.difference(stray_words)

# Print all the common names, that are possible conflicts
print "\nPossible names that conflict:"
common_names = common.difference(institutions)
for name in common_names:
    print name

# Print all the common institutions, that are possible conflicts
print "\nPossible institutions that conflict:"
common_institutions = common.difference(common_names)
for institution in common_institutions:
    print institution
