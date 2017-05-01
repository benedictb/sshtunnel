#! /usr/bin/python

from twisted.internet import reactor
from client_connection import ClientConnectionFactory
from command_connection import CommandHomeConnectionFactory

COMMAND_PORT = 40678
CLIENT_PORT = 41678
DATA_PORT = 42678

# home runs on ash

connections = dict()
reactor.listenTCP(CLIENT_PORT, ClientConnectionFactory(connections))
reactor.listenTCP(COMMAND_PORT, CommandHomeConnectionFactory(connections))

reactor.run()

