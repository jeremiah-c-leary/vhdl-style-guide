
from vsg import parser

###############################################################################
# Entity objects
###############################################################################

class identifier(parser.identifier):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class comma(parser.comma):

    def __init__(self):
        parser.comma.__init__(self)

class colon(parser.colon):

    def __init__(self):
        parser.colon.__init__(self)

class element_subtype_definition(parser.subtype_definition):

    def __init__(self, sString):
        parser.subtype_definition.__init__(self, sString)

class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)

