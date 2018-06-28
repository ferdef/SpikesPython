#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Author: FdF
#

import gevent
from datetime import datetime

def delayed_call():
    gevent.sleep(2)
    print "Executed at",datetime.now()
    
print "Starting at",datetime.now()
gevent.spawn(delayed_call)
gevent.sleep(5)
print "Finished at",datetime.now()
