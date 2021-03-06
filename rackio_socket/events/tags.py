# -*- coding: utf-8 -*-
"""rackio_socket/events/tags.py

This module implements all socket events defined for Tags DAO.
"""

from rackio.dao import LoggerDAO, TagsDAO
from ..core import SocketServer

server = SocketServer()
rs = server.sio

NAMESPACE = "/tags"


@rs.event(namespace=NAMESPACE)
def dbtags(sid):

    logger = LoggerDAO()

    return logger.get_all()


@rs.event(namespace=NAMESPACE)
def tags(sid):

    tags = TagsDAO()

    return tags.get_all()


@rs.event(namespace=NAMESPACE)
def write_tag(sid, data):

    tag_id = data["tag_id"]
    value = data["value"]

    tags = TagsDAO()

    return tags.write(tag_id, value)


@rs.event(namespace=NAMESPACE)
def tag_history(sid, data):

    tag_id = data["tag_id"]

    tags = TagsDAO()

    return tags.get_history(tag_id)


@rs.event(namespace=NAMESPACE)
def tag_trend(sid, data):

    tag_id = data["tag_id"]
    tstart = data["tstart"]
    tstop = data["tstop"]

    tags = TagsDAO()

    return tags.get_trend(tag_id, tstart, tstop)


@rs.event(namespace=NAMESPACE)
def tag_trends(sid, data):

    tags = data["tags"]
    tstart = data["tstart"]
    tstop = data["tstop"]

    tags = TagsDAO()

    return tags.get_trends(tags, tstart, tstop)
