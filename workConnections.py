from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue
from twisted.internet import reactor
from factories import GenericClientFactory

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


class DataConnection(Protocol):
    def __init__(self):
        self.q = DeferredQueue()

    def connectionMade(self):
        reactor.connectTCP('student02.cse.nd.edu', 22, GenericClientFactory(ServiceConnection, self))

    def dataReceived(self, data):
        self.q.put(data)

    def start_forwarding_data(self, service):
        self.service = service
        self.q.get().addCallback(self.forward_data)

    def forward_data(self, data):
        self.service.transport.write(data)
        self.q.get().addCallback(self.forward_data) # Mayhaps this one


class CommandConnection(Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        if data == 'start data connection':
            self.start_data_connection()

    def start_data_connection(self):
        reactor.connectTCP('ash.campus.nd.edu', DATA_PORT, GenericClientFactory(DataConnection))
