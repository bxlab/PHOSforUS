#!/usr/bin/env python

from phosforus import phosforus
import sys

input_line = sys.argv[1:]

if "-m" in input_line:
    if "-v" in input_line:
        phosforus.phosforus(input_line[0], file_input = False, manual_input = True, verbose = True)
    else:
        phosforus.phosforus(input_line[0], file_input = False, manual_input = True)

elif "-d" in input_line:
    if "-v" in input_line:
        phosforus.phosforus(input_line[0], file_input = False, directory_input = True, verbose = True)
    else:
        phosforus.phosforus(input_line[0], file_input = False, directory_input = True)

else:
    if "-v" in input_line:
        phosforus.phosforus(input_line[0], file_input = True, verbose = True)
    else:
        phosforus.phosforus(input_line[0], file_input = True)

