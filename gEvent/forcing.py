#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Author: FdF
#

"""
Forcing to spawn lots of methods
"""

import gevent
from datetime import datetime

def delayed_call():
    gevent.sleep(2)
    print "Ejecutado a las",datetime.now()
    
print "Empezamos a las",datetime.now()
for counter in range(10000):
    gevent.spawn(delayed_call)

print "Termin� a las",datetime.now()
