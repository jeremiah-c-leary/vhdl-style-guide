
from vsg import parser


class when_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class assignment(parser.assignment):

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)


class others_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
