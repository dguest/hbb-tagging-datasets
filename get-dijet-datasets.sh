#!/usr/bin/env bash

set -eu

TAGS=e3569_s2576_s2132_r7725_r7676

function get-datasets() {
    for NUM in {361020..361032}; do
        ami list datasets mc15_13TeV.${NUM}%.merge.AOD.$TAGS
    done
}


function get-datasets-fast() {
    ami list datasets mc15_13TeV.3610%jetjet%.merge.AOD.$TAGS #| grep jetjet_JZ[0-9]W
}
get-datasets-fast
