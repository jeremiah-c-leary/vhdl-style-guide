
from vsg import parser


class subtype_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
