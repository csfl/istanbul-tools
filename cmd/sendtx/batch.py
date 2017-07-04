#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from subprocess import call
from subprocess import Popen
import shlex
import time

ADMIN='c921c91aa4c5f9886bd1e084a848e7e564644d5cc2f265beebb0d51bd251b7e7'
ACCS=40
TX_NUM=50
PERIOD=600
NODES=['http://127.0.0.1:8545', 'http://127.0.0.1:8546', 'http://127.0.0.1:8547', 'http://127.0.0.1:8548']

def file_reader(path):
    """
    Read a file
    """
    with open(path) as data_file:
        data = json.load(data_file)
    return data

def main():
    cmd = './sendtx prepare --addr {} --admin {} --number {}'.format(NODES[0], ADMIN, ACCS)
    call(cmd, shell=True)
    accs = file_reader('accs')
    # wait for money coming
    time.sleep(5)

    processes = []
    n = 0
    for i in range(0,len(accs)):
        cmd = './sendtx batch --addr {} --admin {} --count {} --period {}'.format(NODES[n%len(NODES)], accs[i], TX_NUM, PERIOD)
        processes.append(Popen(shlex.split(cmd)))
	n = n+1

    for p in processes:
        p.wait()

if __name__ == '__main__':
    main()