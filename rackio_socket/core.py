# -*- coding: utf-8 -*-
"""rackio_socket/core.py

This module implements the core app class and methods for Rackio Socket.
"""

import json

from ._singleton import Singleton
from .worker import SocketWorker

from .decorator import AppendWorker
from .push import PushCore


class SocketCore(Singleton):

    def __init__(self):

        super(SocketCore, self).__init__()

        self.app = None
        self.worker = None
        self.push = PushCore()

    def push_data(self, name, data):

        self.push.push_data(name, data)

    def __call__(self, app=None, port=5000):

        if not app:
            return self
        
        self.app = app
        self.worker = SocketWorker(port)

        app._start_workers = AppendWorker(app._start_workers, self.worker)

