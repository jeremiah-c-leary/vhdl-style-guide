
from vsg import parser


class when_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class else_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


