from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Factory


class GenericClientFactory(ClientFactory):
    def __init__(self, connection, *args):
        self.connection = connection
        self.args = args

    def buildProtocol(self, addr):
        return self.conn(self.args)


class GenericFactory(Factory):
    def __init__(self, connection, *args):
        self.connection = connection
        self.args = args

    def buildProtocol(self, addr):
        return self.conn(self.args)