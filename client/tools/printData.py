#!/usr/bin/env python
# CLI for interacting with interop server.

from __future__ import print_function
import argparse
import datetime
import getpass
import logging
import pprint
import sys
import time

#from auvsi_suas.client.client import AsyncClient
#from auvsi_suas.client.types import Telemetry
#from mavlink_proxy import MavlinkProxy
#from upload_odlcs import upload_odlcs



from auvsi_suas.client import client
from auvsi_suas.client import types

#client = AsyncClient('127.0.0.1:8000', 'testuser', 'testpass')



client = client.Client(url='http://127.0.0.1:8000',
                       username='testuser',
                       password='testpass')


missions = client.get_missions()
print(missions)

stationary_obstacles = client.get_obstacles()
print(stationary_obstacles)
