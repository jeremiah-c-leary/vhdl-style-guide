
from vsg import parser


class transport_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class inertial_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class reject_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
