
from vsg import parser


class entity_class(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)
