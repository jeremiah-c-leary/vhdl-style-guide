
from vsg import parser

###############################################################################
# Entity objects
###############################################################################

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class of_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class type_mark(parser.type_mark):

    def __init__(self, sString):
        parser.type_mark.__init__(self, sString)
