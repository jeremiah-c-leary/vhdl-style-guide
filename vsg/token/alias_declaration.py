
from vsg import parser


class alias_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class alias_designator(parser.designator):

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)


class name(parser.name):

    def __init__(self, sString):
        parser.name.__init__(self, sString)
