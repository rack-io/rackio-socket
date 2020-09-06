# -*- coding: utf-8 -*-
"""rackio_socket/core.py

This module implements the core app class and methods for Rackio Socket.
"""
from threading import Thread

from .server import ServerSocket
from eventlet import wsgi, listen


class SocketWorker(Thread):

    def __init__(self, port, *args, **kwargs):

        super(SocketWorker, self).__init__(*args, **kwargs)

        self.port = port
        self.invoker = ServerSocket()

    def run(self):

        wsgi.server(listen(('', self.port)), self.invoker)
    