
from vsg import parser

class range_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

# jcl - remove the following objects after the new parser is done.

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
