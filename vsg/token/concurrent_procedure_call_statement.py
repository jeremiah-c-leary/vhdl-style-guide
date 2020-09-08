
from vsg import parser


class label_name(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):

    def __init__(self):
        parser.label_colon.__init__(self)


class postponed_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
