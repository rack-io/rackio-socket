# -*- coding: utf-8 -*-
"""rackio_socket/events.py

This module implements all socket events defined for Rackio Socket.
"""
from rackio.dao import *
from .core import SocketServer

server = SocketServer()
rs = server.sio


@rs.event
def connect(sid, environ):
    print("connect " , sid)
    rs.emit("welcome", {"message": "Welcome to RackioSocket, the SocketIO server for Rackio!"})


@rs.event
def disconnect(sid):
    print("disconnect " , sid)


@rs.event
def dbtags(sid):

    logger = LoggerDAO()

    return logger.get_all()


@rs.event
def tags(sid):

    tags = TagsDAO()

    return tags.get_all()


@rs.event
def write_tag(sid, data):

    tag_id = data["tag_id"]
    value = data["value"]

    tags = TagsDAO()

    return tags.write(tag_id, value)


@rs.event
def tag_history(sid, data):

    tag_id = data["tag_id"]

    tags = TagsDAO()

    return tags.get_history(tag_id)


@rs.event
def tag_trend(sid, data):

    tag_id = data["tag_id"]
    tstart = data["tstart"]
    tstop = data["tstop"]

    tags = TagsDAO()

    return tags.get_trend(tag_id, tstart, tstop)


@rs.event
def tag_trends(sid, data):

    tags = data["tags"]
    tstart = data["tstart"]
    tstop = data["tstop"]

    tags = TagsDAO()

    return tags.get_trends(tags, tstart, tstop)
