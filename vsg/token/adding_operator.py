
from vsg import parser


class operator(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class plus(operator):

    def __init__(self, sString='+'):
        operator.__init__(self, '+')


class minus(operator):

    def __init__(self, sString='-'):
        operator.__init__(self, '-')


class concat(operator):

    def __init__(self, sString='&'):
        operator.__init__(self, '&')
