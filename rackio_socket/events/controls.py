# -*- coding: utf-8 -*-
"""rackio_socket/events/controls.py

This module implements all socket events defined for Controls DAO.
"""

from rackio.dao import *
from ..core import SocketServer

server = SocketServer()
rs = server.sio
