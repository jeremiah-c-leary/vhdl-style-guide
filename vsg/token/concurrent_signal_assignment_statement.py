
from vsg import parser


class postponed_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class label_name(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)

class label_colon(parser.colon):

    def __init__(self):
        parser.colon.__init__(self)
