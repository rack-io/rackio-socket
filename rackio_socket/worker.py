# -*- coding: utf-8 -*-
"""rackio_socket/core.py

This module implements the core app class and methods for Rackio Socket.
"""
import eventlet

from threading import Thread


class SocketWorker(Thread):

    def __init__(self, sio, port, *args, **kwargs):

        super(SocketWorker, self).__init__(*args, **kwargs)

        self.sio = sio
        self.port = port

    def run(self):

        # wsgi.server(listen(('', self.port)), self.invoker)
        eventlet.wsgi.server(eventlet.listen(('', self.port)), self.sio)
    