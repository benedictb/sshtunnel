from twisted.internet.protocol import ClientFactory, Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from client_connection import ClientConnectionFactory

# 40678 is for command, 41678 is for client, 42678 is for data (and 2 is for SSH)
COMMAND_PORT = 40678
CLIENT_PORT = 41678
DATA_PORT = 42678

class CommandWork(Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        print data


class CommandWorkFactory(ClientFactory):
    def __init__(self, connections):
        self.conn = CommandWork
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn
        self.connections['cmd'] = c
        return c


class CommandHome(Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        self.start_client_connection()

    def dataReceived(self, data):
        print data

    def start_client_connection(self):
        reactor.listenTCP(CLIENT_PORT, ClientConnectionFactory(self.connections))


class CommandHomeFactory(Factory):
    def __init__(self, connections):
        self.conn = CommandHome
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn()
        self.connections['cmd'] = c
        return self.conn





