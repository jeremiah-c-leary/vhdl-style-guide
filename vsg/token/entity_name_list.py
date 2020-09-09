
from vsg import parser


class others_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class all_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class comma(parser.comma):

    def __init__(self, sString=','):
        parser.comma.__init__(self)
