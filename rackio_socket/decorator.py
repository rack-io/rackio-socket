# -*- coding: utf-8 -*-
"""rackio_socket/decorator.py

This module implements the decorator's for worker
execution of Rackio Socket.
"""
import types


class AppendWorker(object):

    def __init__(self, f, worker):
        self.func = f
        self.worker = worker

    def __get__(self, instance, cls):
       return types.MethodType(self, instance)

    def __call__(self, *args, **kwargs):
        
        self.func(*args, **kwargs)

        self.worker.daemon = True
        self.worker.start()
        