from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118


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
