#! /bin/bash

if ! [[ -x ugrep ]]; then
    echo "ugrep executable does not exist" >&2
    exit 1
fi

bash ../tester/run-tests.sh "$@"
