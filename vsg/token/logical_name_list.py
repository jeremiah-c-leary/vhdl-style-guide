
from vsg import parser


class logical_name(parser.logical_name):

    def __init__(self, sString):
        parser.logical_name.__init__(self, sString)

class comma(parser.comma):

    def __init__(self, sString=','):
        parser.comma.__init__(self)
