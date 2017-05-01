from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Factory


class genericClientFactory(ClientFactory):
    def __init__(self, connection, *args):
        self.conn = connection
        self.args = args

    def buildProtocol(self, addr):
        return self.conn(*self.args)


class genericFactory(Factory):
    def __init__(self, connection, *args):
        self.conn = connection
        self.args = args

    def buildProtocol(self, addr):
        return self.conn(*self.args)
