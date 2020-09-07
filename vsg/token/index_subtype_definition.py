from vsg import parser


class range_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class undefined_range(parser.undefined_range):

    def __init__(self, sString='<>'):
        parser.undefined_range.__init__(self)
