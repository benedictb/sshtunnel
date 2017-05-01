from twisted.internet.protocol import ClientFactory, Factory
from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue
from twisted.internet import reactor

from service_connection import ServiceConnectionFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118


# This is the what waits for the data connection
# It waits for the data to come in on Home

class DataHomeConnection(Protocol):
    def __init__(self, client):
        self.client = client

    def connectionMade(self):
        self.client.start_forwarding_client_data(self)

    def dataReceived(self, data):
#        print 'outgoing:\n' + data
        self.client.transport.write(data)


class DataHomeConnectionFactory(Factory):
    def __init__(self, client):
        self.conn = DataHomeConnection
        self.client = client

    def buildProtocol(self, addr):
        return self.conn(self.client)


# This is the client for data
class DataWorkConnection(Protocol):
    def __init__(self):
        self.q = DeferredQueue()

    def connectionMade(self):
        reactor.connectTCP('student02.cse.nd.edu', 22, ServiceConnectionFactory(self))

    def dataReceived(self, data):
        self.q.put(data)

    def start_forwarding_data(self, service):
        self.service = service
        self.q.get().addCallback(self.forward_data)

    def forward_data(self, data):
        self.service.transport.write(data)
        self.q.get().addCallback(self.forward_data) # Mayhaps this one

class DataWorkConnectionFactory(ClientFactory):
    def __init__(self):
        self.conn = DataWorkConnection

    def buildProtocol(self, addr):
        return self.conn()


