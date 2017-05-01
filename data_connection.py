from twisted.internet.protocol import ClientFactory, Factory
from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue

# 40678 is for command, 41678 is for client, 42678 is for data (and 2 is for SSH)
COMMAND_PORT = 40678
CLIENT_PORT = 41678
DATA_PORT = 42678


# This is the what waits for the data connection
# It waits for the data to come in on Home

class DataHomeConnection(Protocol):
    def __init__(self, connections):
        self.connections = connections

    def connectionMade(self):
        self.connections['client'].start_forwarding_client_data()

    def dataReceived(self, data):
        self.connections['client'].transport.write(data)


class DataHomeConnectionFactory(Factory):
    def __init__(self, connections):
        self.conn = DataHomeConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn(self.connections)
        self.connections['service'] = c
        return c


# This is the client for data
class DataWorkConnection(Protocol):
    def __init__(self, connections):
        self.connections = connections
        self.q = DeferredQueue()

    def connectionMade(self):
        self.connections['service'].start_forwarding_service_data()

    def dataReceived(self, data):
        self.connections['service'].write(data)



class DataWorkConnectionFactory(ClientFactory):
    def __init__(self, connections):
        self.conn = DataWorkConnection
        self.connections = connections

    def buildProtocol(self, addr):
        c = self.conn(self.connections)
        self.connections['service'] = c
        return c


