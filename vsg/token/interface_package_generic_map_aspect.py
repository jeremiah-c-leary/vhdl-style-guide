
from vsg import parser


class generic_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class map_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):

    def __init__(self, sString=')'):
        parser.open_parenthesis.__init__(self)


class default_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class undefined_range(parser.undefined_range):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class close_parenthesis(parser.close_parenthesis):

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)
