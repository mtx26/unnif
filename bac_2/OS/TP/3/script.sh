#!/bin/bash
for arg in "$@"; do
    echo $arg
done

for (( i=1; i <= $#; i++ )); do
    echo "${!i}"
done

while (( $# > 0 )); do
    echo $1
    shift
done