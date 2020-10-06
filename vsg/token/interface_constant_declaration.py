
from vsg import parser


class constant_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class subtype_indication(parser.subtype_indication):
    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class assignment(parser.assignment):

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)
