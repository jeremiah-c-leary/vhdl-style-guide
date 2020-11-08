
from vsg import parser


class sign(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class plus(sign):

    def __init__(self, sString='+'):
        sign.__init__(self, '+')


class minus(sign):

    def __init__(self, sString='-'):
        sign.__init__(self, '-')
