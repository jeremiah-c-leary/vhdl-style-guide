
from vsg import parser


class comma(parser.comma):

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)
