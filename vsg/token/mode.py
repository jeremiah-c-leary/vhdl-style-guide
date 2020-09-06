
from vsg import parser


class in_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class out_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class inout_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class buffer_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class linkage_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
