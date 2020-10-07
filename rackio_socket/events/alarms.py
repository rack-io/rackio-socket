# -*- coding: utf-8 -*-
"""rackio_socket/events/alarms.py

This module implements all socket events defined for Alarms DAO.
"""

from rackio.dao import AlarmsDAO
from ..core import SocketServer

server = SocketServer()
rs = server.sio


@rs.event
def alarms(sid):

    dao = AlarmsDAO()

    return dao.get_all()


@rs.event
def alarm(sid, data):

    name = data["alarm_name"]

    dao = AlarmsDAO()

    return dao.get(name)


@rs.event
def update_alarm(sid, data):

    name = data["alarm_name"]
    action = data["action"]

    dao = AlarmsDAO()

    return dao.update(name, action)
