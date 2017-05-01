#! /usr/bin/python

from twisted.internet import reactor
from factories import genericClientFactory
from workConnections import *

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

# reactor.connectTCP('ash.campus.nd.edu', COMMAND_PORT, CommandWorkConnectionFactory())
reactor.connectTCP('ash.campus.nd.edu', COMMAND_PORT, genericClientFactory(CommandWorkConnection))

reactor.run()

