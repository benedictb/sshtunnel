from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118


class ServiceConnection(Protocol):
    def __init__(self, data):
        self.q = DeferredQueue()
        self.data = data

    def connectionMade(self):
        self.data.start_forwarding_data(self)

    def dataReceived(self, data):
        self.data.transport.write(data)


class ServiceConnectionFactory(ClientFactory):
    def __init__(self, data):
        self.conn = ServiceConnection
        self.data = data

    def buildProtocol(self, addr):
        return self.conn(self.data)
