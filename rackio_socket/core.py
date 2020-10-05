# -*- coding: utf-8 -*-
"""rackio_socket/core.py

This module implements the core app class and methods for Rackio Socket.
"""

import eventlet
import json
import socketio

from ._singleton import Singleton
from .worker import SocketWorker

from .decorator import AppendWorker
from .push import PushCore


class SocketServer(Singleton):

    def __init__(self):
    
        super(SocketServer, self).__init__()

        self.sio = socketio.Server(cors_allowed_origins='*')


class SocketCore(Singleton):

    def __init__(self):

        super(SocketCore, self).__init__()

        self.app = None
        self.server = SocketServer()

    def __call__(self, app=None, port=5000):

        if not app:
            return self.server.sio

        sio = self.server.sio

        print(app._api_manager.app)

        self.app = socketio.WSGIApp(sio)

        eventlet.wsgi.server(eventlet.listen(('', port)), self.app)


