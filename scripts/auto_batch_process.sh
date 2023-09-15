#!/bin/bash

to_be_processed_dir=$1

# if is empty, set to TO_BE_PROCESSED_DIR
if [ -z "$to_be_processed_dir" ]
then
    echo "Empty argument, set to TO_BE_PROCESSED"
    to_be_processed_dir=TO_BE_PROCESSED
fi

echo "Working directory: $PWD, to_be_processed_dir: $to_be_processed_dir"

files=$(find $to_be_processed_dir -name "*.bib")

# 1. remove duplicate entries
echo "1. Removing duplicate entries..."
for file in $files
do
    echo "Processing $file"
    bibtex-tidy $file --modify
done

# 2. change full names to abbreviations
echo "2. Changing full names to abbreviations..."
echo $files
python3 pyscripts/rename.py $files
