
from vsg import parser


class open_bracket(parser.open_bracket):

    def __init__(self, sString='['):
        parser.open_bracket.__init__(self, '[')


class return_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class comma(parser.comma):

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class close_bracket(parser.close_bracket):

    def __init__(self, sString=']'):
        parser.close_bracket.__init__(self, ']')
