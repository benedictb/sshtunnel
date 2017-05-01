#! /usr/bin/python

from twisted.internet import reactor
from command_connection import CommandHomeConnectionFactory
from factories import genericFactory
from homeConnections import *

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

# reactor.listenTCP(COMMAND_PORT, CommandHomeConnectionFactory())
reactor.listenTCP(COMMAND_PORT, genericFactory(CommandHomeConnection))
reactor.run()

