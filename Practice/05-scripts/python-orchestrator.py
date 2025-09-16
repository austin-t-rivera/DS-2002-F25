#!/usr/bin/env python3


# How to run a bash command from within a python3 script.


## -----------------------------------------------------------
## BAD
## This solution looks simple but is a bad practice. os.system
## and os.spawn have been dropped. So this may not work on newer
## systems.

import os
bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
os.system(bashCommand)



## -----------------------------------------------------------
## GOOD
## A simple example with static quote-wrapped inputs:

import subprocess

cmd = "bash detabify.sh mock_data.tsv output.csv"
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()



## -----------------------------------------------------------
## BETTER
## This allows you to pass variables into the bash command:

import subprocess
import os

# Set variables someplace
INPUT = 'mock_data.tsv'
OUTPUT = 'output.csv'

# Now use string substitution in the command
cmd = f'bash detabify.sh {INPUT} {OUTPUT}'
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
