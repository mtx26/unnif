#!/bin/bash

first=1
for arg in "$@"; do
    for line in $(cat "$arg"); do
        if ((first)); then
            max=$line
            file=$arg
            first=0

        elif ((line > max)); then
            max=$line
            file=$arg
        fi
    done < "$arg"
done
echo "$max"
echo "$file"
