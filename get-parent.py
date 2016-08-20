#!/usr/bin/env python3

import sys, json

LDN='logicalDatasetName'

def _get_this(prov):
    for ds in prov:
        if ds['distance'] == '0':
            return ds

def _get_evt(prov):
    this_dsid = _get_this(prov)[LDN].split('.')[1]
    for ds in prov:
        if this_dsid in ds[LDN] and ds['dataType'] == 'EVNT':
            return ds

for line in sys.stdin:
    prov = json.loads(line)
    evt = _get_evt(prov)
    sys.stdout.write(evt[LDN] + '\n')

