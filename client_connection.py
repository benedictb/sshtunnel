from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue
from twisted.internet import reactor

from data_connection import DataHomeConnectionFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

class ClientConnection(Protocol):
    def __init__(self, connections):
        self.connections = connections
        self.q = DeferredQueue()

    def connectionMade(self):
        reactor.listenTCP(DATA_PORT, DataHomeConnectionFactory(self.connections))
        self.connections['cmd'].transport.write('start data connection')

    def dataReceived(self, data):
        print 'incoming:\n' + data 
        self.q.put(data)

    def start_forwarding_client_data(self):
        self.q.get().addCallback(self.forward_data)

    def forward_data(self, data):
        self.connections['data'].transport.write(data)


class ClientConnectionFactory(Factory):
    def __init__(self, connections):
        self.conn = ClientConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn(self.connections)
        self.connections['client'] = c
        return c
