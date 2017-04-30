from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol


class ClientConnection(Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        print data


class ClientConnectionFactory(Factory):
    def __init__(self, connections):
        self.conn = ClientConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn()
        self.connections['client'] = c
        return c
