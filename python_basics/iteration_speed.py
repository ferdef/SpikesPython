#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Author: FdF
#

def tryway():
    alist = range(1000)
    try:
        while True:
            yield alist.pop()
    except IndexError:
        pass

def whileway():
    alist = range(1000)
    while alist:
        yield alist.pop()

def forway():
    alist = range(1000)
    for item in alist:
        yield item

if __name__=='__main__':
    from timeit import Timer
    print "Testing Try"
    tr = Timer("list(tryway())","from __main__ import tryway")
    print tr.timeit(10000)
    print "Testing while"
    ir = Timer("list(whileway())","from __main__ import whileway")
    print ir.timeit(10000)
    print "Testing for"
    ir = Timer("list(forway())","from __main__ import forway")
    print ir.timeit(10000)
