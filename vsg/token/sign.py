
from vsg import parser


class sign(parser.item):

    def __init__(self, sString):
        parser.sign.__init__(self, sString)


class plus_sign(sign):

    def __init__(self, sString):
        sign.__init__(self, '+')


class minus_sign(sign):

    def __init__(self, sString):
        sign.__init__(self, '-')
