# -*- coding: utf-8 -*-
"""rackio_socket/push.py

This module implements the Push Core for Rackio Socket.
"""
from ._singleton import Singleton


class PushCore(Singleton):

    def __init__(self):

        self.data = dict()

    def get_data(self):

        return self.data

    def push_data(self, name, value):

        self.data[name] = value
    