from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue
from twisted.internet import reactor

from data_connection import DataHomeConnectionFactory

COMMAND_PORT = 40118
CLIENT_PORT = 42118
DATA_PORT = 41118

class ClientConnection(Protocol):
    def __init__(self, cmd):
        self.cmd = cmd
        self.q = DeferredQueue()

    def connectionMade(self):
        reactor.listenTCP(DATA_PORT, DataHomeConnectionFactory(self))
        self.cmd.transport.write('start data connection')

    def dataReceived(self, data):
        self.q.put(data)

    def start_forwarding_client_data(self, data):
        self.data = data
        self.q.get().addCallback(self.forward_data)

    def forward_data(self, data):
        self.data.transport.write(data)
        self.q.get().addCallback(self.forward_data)



class ClientConnectionFactory(Factory):
    def __init__(self, cmd):
        self.conn = ClientConnection
        self.cmd = cmd

    def buildProtocol(self, addr):
        return self.conn(self.cmd)

