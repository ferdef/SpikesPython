#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Author: FdF
#

from ctypes import cdll
lib = cdll.LoadLibrary('./libmain.so')

def get_value():
    print lib.getValue(5)

if __name__=='__main__':
    get_value()
