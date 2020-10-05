# -*- coding: utf-8 -*-
"""rackio_socket/events.py

This module implements all socket events defined for Rackio Socket.
"""

from .core import SocketCore

rs = SocketCore()

@rs.event
def connect(sid, environ):
    print("connect " , sid)
    rs.emit("welcome", {"message": "Welcome to RackioSocket, the SocketIO server for Rackio!"})

@rs.event
def disconnect(sid, environ):
    print("disconnect " , sid)
