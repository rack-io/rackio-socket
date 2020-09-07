# -*- coding: utf-8 -*-
"""rackio_socket/server.py

This module implements the core Server Class for Rackio Socket.
"""
import json
import time
import random

from threading import Thread
from queue import Queue

from eventlet import websocket

from .push import PushCore


class ServerSocket:

    @websocket.WebSocketWSGI
    def __call__(self):

        from rackio import Rackio, TagEngine

        app = Rackio()
        tag_engine = TagEngine()
        push_core = PushCore()

        while True:

            duration = random.random() / 10
            time.sleep(duration)

            result = dict()
            result["summary"] = app.summary()
            result["tags"] = tag_engine.serialize()

            values = push_core.get_data()

            for name, value in values.items():

                result[name] = value
            
            message = json.dumps(result)
            self.send(message)
            