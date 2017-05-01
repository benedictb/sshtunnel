#! /usr/bin/python
# Benedict Becker
# bbecker5
# twisted primer

from twisted.internet import reactor
from factories import GenericFactory
from homeConnections import CommandConnection

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

reactor.listenTCP(COMMAND_PORT, GenericFactory(CommandConnection))
reactor.run()

