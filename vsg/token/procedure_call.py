
from vsg import parser


class procedure_name(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
