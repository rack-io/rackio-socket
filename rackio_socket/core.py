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


class SocketServer(Singleton):

    def __init__(self):
    
        super(SocketServer, self).__init__()

        self.sio = socketio.Server(cors_allowed_origins='*')


class SocketCore(Singleton):

    def __init__(self):

        super(SocketCore, self).__init__()

        self.app = None
        self.port = None
        self.server = SocketServer()

    def __call__(self, app=None, port=5000):

        if not app:
            return self.server.sio

        self.app = app
        self.port = port

        sio = self.server.sio

        self.sio_app = socketio.WSGIApp(sio)

        self.worker = SocketWorker(self.sio_app, port)

        app._start_workers = AppendWorker(app._start_workers, self.worker)
    