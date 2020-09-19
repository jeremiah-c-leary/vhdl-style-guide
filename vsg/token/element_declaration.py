
from vsg import parser


class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
