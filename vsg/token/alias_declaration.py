
from vsg import parser

###############################################################################
# Entity objects
###############################################################################

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class character_literal(parser.character_literal):

    def __init__(self, sString):
        parser.character_literal.__init__(self, sString)


class operator_symbol(parser.operator_symbol):

    def __init__(self, sString):
        parser.character_literal.__init__(self, sString)


class colon(parser.colon):

    def __init__(self):
        parser.colon.__init__(self)


class subtype_indication(parser.subtype_indication):

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class name(parser.name):

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class signature(parser.signature):

    def __init__(self, sString):
        parser.signature.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
