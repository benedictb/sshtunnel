#! /usr/bin/python

from twisted.internet import reactor
from command_connection import CommandHomeConnectionFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

# home runs on ash

reactor.listenTCP(COMMAND_PORT, CommandHomeConnectionFactory())

reactor.run()

