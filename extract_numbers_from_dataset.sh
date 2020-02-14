#!/bin/bash
cat $1| grep -E -o "[0-9]+"

# Execute like this:
# ./extract_numbers_from_dataset.sh <some_dataset_file>
#
# And copy the output into any  benford's law calculator, like:
# https://www.dcode.fr/benford-law
# http://first-digit.appspot.com/
# https://github.com/evancolvin/Benfords-Law
# https://github.com/carloscinelli/benford.analysis
