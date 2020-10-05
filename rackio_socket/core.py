# -*- coding: utf-8 -*-
"""rackio_socket/core.py

This module implements the core app class and methods for Rackio Socket.
"""

import json
import socketio

from ._singleton import Singleton
from .worker import SocketWorker

from .decorator import AppendWorker
from .push import PushCore


class SocketCore(Singleton):

    def __init__(self):

        super(SocketCore, self).__init__()

        self.app = None
        self.sio = socketio.Server()

    def __call__(self, app=None, port=5000):

        if not app:
            return self
        
        self.app = socketio.WSGIApp(self.sio, app._api_manager.app)

    def event(self):

        return self.sio.event

    def on(self):

        return self.sio.event

    def emit(self):

        return self.sio.emit

    
