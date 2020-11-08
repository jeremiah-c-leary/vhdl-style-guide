
from vsg import parser


class operator(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class plus(operator):

    def __init__(self, sString='+'):
        operator.__init__(self, '+')


class minus(operator):

    def __init__(self, sString='-'):
        operator.__init__(self, '-')


class concat(operator):

    def __init__(self, sString='&'):
        operator.__init__(self, '&')
