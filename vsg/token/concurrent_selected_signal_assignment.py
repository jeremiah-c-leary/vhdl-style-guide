
from vsg import parser


class with_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class select_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class target(parser.target):

    def __init__(self, sString):
        parser.target.__init__(self, sString)


class assignment(parser.assignment):

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)


class guarded_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
