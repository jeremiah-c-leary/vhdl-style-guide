
from vsg import parser


class simple_expression(parser.simple_expression):

    def __init__(self, sString):
        parser.simple_expression.__init__(self, sString)


class direction(parser.direction):

    def __init__(self, sString):
        parser.direction.__init__(self, sString)
