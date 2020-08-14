
from vsg import parser


class when_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class comma(parser.keyword):

    def __init__(self):
        parser.comma.__init__(self)
