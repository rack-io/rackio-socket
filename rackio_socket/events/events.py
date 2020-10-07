# -*- coding: utf-8 -*-
"""rackio_socket/events/events.py

This module implements all socket events defined for Events DAO.
"""

from rackio.dao import EventsDAO
from ..core import SocketServer

server = SocketServer()
rs = server.sio


@rs.event
def events(sid):

    dao = EventsDAO()

    return dao.get_all()


@rs.event
def publish_event(sid, data):

    user = data["user"]
    message = data["message"]
    description = data["description"]
    priority = data["priority"]

    dao = EventsDAO()

    return dao.write(user, message, description, priority)
