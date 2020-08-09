
from vsg import parser

###############################################################################
# Entity objects
###############################################################################

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class end_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class record_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class simple_name(parser.simple_name):

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)

class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
