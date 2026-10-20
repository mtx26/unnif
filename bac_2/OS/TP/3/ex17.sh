#!/bin/bash

for arg in "$@"; do
    if [[ -e $arg ]]; then
        if [[ -d $arg ]]; then
            echo "$arg :"
            ls $arg
        else
            echo "$arg :"
            cat $arg
            echo \n
        fi
    else
        echo "$arg non existant"
    fi
done