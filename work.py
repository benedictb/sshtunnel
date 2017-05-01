#! /usr/bin/python

from twisted.internet import reactor
from command_connection import CommandWorkConnectionFactory
import sys

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

# work runs on newt

reactor.connectTCP('ash.campus.nd.edu', COMMAND_PORT, CommandWorkConnectionFactory())
reactor.run()

