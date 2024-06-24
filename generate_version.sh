#!/bin/bash -e 

# Any commands which fail will cause the shell script to exit immediately 
set -e 

# See the commands executed in the command window 
set -x 

CURRENT_DATE=$(date +%Y.%m)
VERSION="$CURRENT_DATE"

echo "Generated release version: $VERSION"
echo $VERSION  # Output the version for use in other commands