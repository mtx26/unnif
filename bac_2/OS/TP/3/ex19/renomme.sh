#!/bin/bash
name=$1
shift
i=1
for arg in "$@"; do
    if [[ -f $arg ]]; then
        while [[ -f "${name}${i}" ]]; do
            ((i++))
        done
        mv $arg "${name}${i}"
        ((i++))
    fi
done

        
