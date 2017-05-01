from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue
from twisted.internet import reactor
from factories import GenericFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118


class ClientConnection(Protocol):
    def __init__(self, cmd):
        self.cmd = cmd
        self.q = DeferredQueue()

    def connectionMade(self):
        reactor.listenTCP(DATA_PORT, GenericFactory(DataConnection, self))
        self.cmd.transport.write('start data connection')

    def dataReceived(self, data):
        self.q.put(data)

    def start_forwarding_client_data(self, data):
        self.data = data
        self.q.get().addCallback(self.forward_data)

    def forward_data(self, data):
        self.data.transport.write(data)
        self.q.get().addCallback(self.forward_data)


class DataConnection(Protocol):
    def __init__(self, client):
        self.client = client

    def connectionMade(self):
        self.client.start_forwarding_client_data(self)

    def dataReceived(self, data):
        self.client.transport.write(data)


class CommandConnection(Protocol):
    def __init__(self):
        reactor.listenTCP(CLIENT_PORT, GenericFactory(ClientConnection))

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        pass
