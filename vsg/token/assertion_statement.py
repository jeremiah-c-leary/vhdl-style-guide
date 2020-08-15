
from vsg import parser


class assert_label(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class assert_label_colon(parser.label_colon):

    def __init__(self):
        parser.label_colon.__init__(self)


class assert_semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
