from twisted.internet.protocol import ClientFactory, Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from data_connection import DataWorkConnectionFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

class CommandWorkConnection(Protocol):
    def __init__(self, connections):
        self.connections = connections

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        if data == 'start data connection':
            self.start_data_connection()

    def start_data_connection(self):
        reactor.connectTCP('ash.campus.nd.edu', DATA_PORT, DataWorkConnectionFactory(self.connections))

class CommandWorkConnectionFactory(ClientFactory):
    def __init__(self, connections):
        self.conn = CommandWorkConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn(self.connections)
        self.connections['cmd'] = c
        return c


class CommandHomeConnection(Protocol):
    def __init__(self, connections):
        self.connections = connections

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        pass


class CommandHomeConnectionFactory(Factory):
    def __init__(self, connections):
        self.conn = CommandHomeConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn(self.connections)
        self.connections['cmd'] = c
        return c





