#! /usr/bin/python
# Benedict Becker
# bbecker5
# twisted primer

from twisted.internet import reactor
from factories import GenericClientFactory
from workConnections import CommandConnection

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

reactor.connectTCP('ash.campus.nd.edu', COMMAND_PORT, GenericClientFactory(CommandConnection))
reactor.run()

