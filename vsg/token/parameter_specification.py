
from vsg import parser


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class in_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
