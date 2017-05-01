from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.defer import DeferredQueue
from data_connection import DataWorkConnectionFactory

COMMAND_PORT = 40678
CLIENT_PORT = 41678
DATA_PORT = 42678


class ServiceConnection(Protocol):
    def __init__(self, connections):
        self.connections = connections
        self.q = DeferredQueue()
        
    def connectionMade(self):
        self.connections['data'].start_forwarding_data()

    def dataReceived(self, data):
        self.connections['data'].transport.write(data)


class ServiceConnectionFactory(ClientFactory):
    def __init__(self, connections):
        self.conn = ServiceConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn(self.connections)
        self.connections['service'] = c
        return c
