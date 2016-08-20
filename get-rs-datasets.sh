#!/usr/bin/env bash

set -eu

TAGS=e3820_s2608_s2183_r7772_r7676

function get-datasets() {
    for NUM in {301488..301507}; do
        ami list datasets mc15_13TeV.${NUM}%.merge.AOD.$TAGS
    done
}
