# -*- coding: utf-8 -*-
"""rackio_socket/core.py

This module implements the core app class and methods for Rackio Socket.
"""
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import socketio

from threading import Thread


class SocketWorker(Thread):

    def __init__(self, sio, port, *args, **kwargs):

        super(SocketWorker, self).__init__(*args, **kwargs)

        self.sio = sio
        self.port = port

    def run(self):

        app = socketio.WSGIApp(self.sio)
        pywsgi.WSGIServer(('', self.port), app,
            handler_class=WebSocketHandler).serve_forever()


