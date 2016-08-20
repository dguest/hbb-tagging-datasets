#!/usr/bin/env bash

set -eu

function get-evt-parent() {
    ami -f json show dataset prov $1 | head -n1 | ./get-parent.py
}

if (( $# == 0 )); then
    echo "ERROR: give me a list of datasets" >&2
    exit 0
fi

for DS in $(cat $1) ; do
    PARENT=$(get-evt-parent $DS)
    echo "parent: $PARENT"
    ami -f json show dataset info $PARENT | ./build-ds-entry.py
done
