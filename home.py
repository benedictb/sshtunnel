#! /usr/bin/python

from twisted.internet import reactor
from client_connection import ClientConnectionFactory
from command_connection import CommandHomeConnectionFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

# home runs on ash

cmd = CommandHomeConnectionFactory()
reactor.listenTCP(COMMAND_PORT, cmd)
reactor.listenTCP(CLIENT_PORT, ClientConnectionFactory(cmd))

reactor.run()

