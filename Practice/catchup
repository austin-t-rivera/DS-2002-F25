#!/bin/bash

# git pull origin main
state=`git remote -v | grep upstream | wc -l`
if [ "$state" -lt 1 ]
then
    echo "Adding upstream connection"
    git remote add upstream https://github.com/nmagee/ds2002-course.git
fi

git fetch upstream && git merge upstream/main main
clear
echo "Sync with DS2002 repository complete."
