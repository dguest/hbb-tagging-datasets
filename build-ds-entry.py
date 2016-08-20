#!/usr/bin/env python3

"""build a line for the 'database' based on the input json and input
ds name
"""

import sys, json

LDN='logicalDatasetName'

def run_json(json_string):
    info = json.loads(json_string)[0]
    events = info['totalEvents']
    xsec = info.get('crossSection_mean') or info['crossSection']
    filteff = info['GenFiltEff_mean']
    name = info[LDN].split('.')[2].split('_', 2)[-1]
    dsid = info[LDN].split('.')[1]
    outform = '{nm:8}  {dsid}  {xsec:.4E}  {fe:.4E}  {nevt}'.format(
        nm=name, dsid=dsid, xsec=float(xsec), fe=float(filteff), nevt=events)
    sys.stdout.write(outform + '\n')

def run():
    for line in sys.stdin:
        run_json(line.strip())
    sys.stdin.flush()

if __name__ == '__main__':
    run()
