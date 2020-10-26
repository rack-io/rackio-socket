# -*- coding: utf-8 -*-
"""rackio_socket/core.py

This module implements the core app class and methods for Rackio Socket.
"""

import json
import socketio

from ._singleton import Singleton
from .worker import SocketWorker

from .decorator import AppendWorker


class SocketServer(Singleton):

    def __init__(self):
    
        super(SocketServer, self).__init__()

        self.sio = socketio.Server(async_mode='gevent', cors_allowed_origins='*')


class SocketCore(Singleton):

    def __init__(self):

        super(SocketCore, self).__init__()

        self.app = None
        self.port = None
        self.server = SocketServer()

    def get_sio(self):

        return self.server.sio

    def __call__(self, app=None, port=5000):

        if not app:
            return self.server.sio

        self.app = app
        self.port = port

        sio = self.server.sio
        
        self.worker = SocketWorker(sio, port)

        app._start_workers = AppendWorker(app._start_workers, self.worker)
    