# -*- coding: utf-8 -*-
"""rackio_socket/events/alarms.py

This module implements all socket events defined for Alarms DAO.
"""

from rackio.dao import *
from ..core import SocketServer

server = SocketServer()
rs = server.sio
