#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Author: FdF
#

import gevent
from gevent import socket

urls = ['www.google.com', 'www.terra.es', 'gittid.hi.inet']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=15)

print [job.value for job in jobs]
