#!/bin/bash

# 1. shebang / executable
# 2. error out --> set -e / error codes --> || exit 1;
# 3. input parameters
# 4. conditional logic
# 5. environment / full paths
# 6. logging
# 7. comments!

# Input file: mock_data.tsv
#
# Command: tr '\t' ',' < file.tsv > file.csv

# If/Else
echo -n "Enter a number: "
read VAR

if [[ $VAR -gt 10 ]]
then
  echo "The variable is greater than 10."
else
  echo "Your number is pretty small!"
fi
