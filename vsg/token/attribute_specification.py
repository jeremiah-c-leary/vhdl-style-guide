
from vsg import parser


class attribute_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class attribute_designator(parser.designator):

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class of_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
