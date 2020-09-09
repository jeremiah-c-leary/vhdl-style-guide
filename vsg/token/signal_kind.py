
from vsg import parser


class register_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class bus_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
