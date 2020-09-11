
from vsg import parser


class while_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class for_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
