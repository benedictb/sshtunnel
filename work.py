#! /usr/bin/python

from twisted.internet import reactor
from service_connection import ServiceConnectionFactory

connections = dict()

reactor.connectTCP('student02.cse.nd.edu', 22, ServiceConnectionFactory(connections))
reactor.run()

