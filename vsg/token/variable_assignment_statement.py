
from vsg import parser


class label(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.colon):

    def __init__(self, sString=';'):
        parser.colon.__init__(self, sString)
