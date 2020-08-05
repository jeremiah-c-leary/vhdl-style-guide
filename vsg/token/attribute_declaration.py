
from vsg import parser

###############################################################################
# Attribute objects
###############################################################################

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class colon(parser.colon):

    def __init__(self):
        parser.colon.__init__(self)


class type_mark(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
