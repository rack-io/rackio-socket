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

        from rackio import Rackio

        app = Rackio()
        
        while True:

            duration = random.random() / 10
            time.sleep(duration)

            result = dict()
            result["summary"] = app.summary()
            
            message = json.dumps(result)
            self.send(message)
            
            