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
        reactor.connectTCP('ash.campus.nd.edu', DATA_PORT, DataWorkConnectionFactory(self.connections))

    def dataReceived(self, data):
        print data
        self.q.put(data)

    def start_forwarding_service_data(self):
        self.q.get().addCallback(self.forward_data)

    def forward_data(self, data):
        self.connections['data'].transport.write(data)


class ServiceConnectionFactory(ClientFactory):
    def __init__(self, connections):
        self.conn = ServiceConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn(self.connections)
        self.connections['service'] = c
        return c
