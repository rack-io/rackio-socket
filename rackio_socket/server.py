# -*- coding: utf-8 -*-
"""rackio_socket/server.py

This module implements the core Server Class for Rackio Socket.
"""
import json
import time
import random

from threading import Thread

from eventlet import websocket


class ServerSocket:

    @websocket.WebSocketWSGI
    def __call__(self):

        self.variable = 0
        
        while True:
            duration = random.random() / 100
            time.sleep(duration)
            random_increment = int(random.random() * 10) + 1
            self.variable += random_increment
            message = json.dumps({'variable': self.variable})
            self.send(message)