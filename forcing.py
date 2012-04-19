#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Author: FdF (cano266)
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

print "Terminó a las",datetime.now()
