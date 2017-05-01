from twisted.internet.protocol import ClientFactory, Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from data_connection import DataWorkConnectionFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

class CommandWorkConnection(Protocol):
    def __init__(self, service):
        pass

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        if data == 'start data connection':
            self.start_data_connection()

    def start_data_connection(self):
        reactor.connectTCP('ash.campus.nd.edu', DATA_PORT, DataWorkConnectionFactory())

class CommandWorkConnectionFactory(ClientFactory):
    def __init__(self):
        self.conn = CommandWorkConnection

    def buildProtocol(self, addr):
        return self.conn()


class CommandHomeConnection(Protocol):
    def __init__(self, connections):
        pass

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        pass


class CommandHomeConnectionFactory(Factory):
    def __init__(self):
        self.conn = CommandHomeConnection

    def buildProtocol(self, addr):
        return self.conn()





