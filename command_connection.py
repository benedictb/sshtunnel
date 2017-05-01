from twisted.internet.protocol import ClientFactory, Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from client_connection import ClientConnectionFactory
from service_connection import ServiceConnectionFactory

# 40678 is for command, 41678 is for client, 42678 is for data (and 2 is for SSH)
COMMAND_PORT = 40678
CLIENT_PORT = 41678
DATA_PORT = 42678

# If the work cmd connect receives start data connect, start the service connect


class CommandWorkConnection(Protocol):
    def __init__(self, connections):
        self.connections = connections

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        if data == 'start data connection':
            self.start_service_connection()

    def start_service_connection(self):
        reactor.connectTCP('student02.cse.nd.edu', 22, ServiceConnectionFactory(self.connections))


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
        return self.conn





