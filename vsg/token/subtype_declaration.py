
from vsg import parser

###############################################################################
# Subtype objects
###############################################################################

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)

class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class subtype_indication(parser.subtype_indication):

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)

class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
