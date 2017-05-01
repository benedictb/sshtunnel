#! /usr/bin/python

from twisted.internet import reactor
from command_connection import CommandWorkConnectionFactory

COMMAND_PORT = 40678
CLIENT_PORT = 41678
DATA_PORT = 42678

connections = dict()
reactor.connectTCP('ash.campus.nd.edu', COMMAND_PORT, CommandWorkConnectionFactory(connections))
reactor.run()

