
from vsg import parser


class after_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class null_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
