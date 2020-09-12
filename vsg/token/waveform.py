
from vsg import parser


class comma(parser.comma):

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class unaffected_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
