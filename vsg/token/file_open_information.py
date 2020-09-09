
from vsg import parser


class open_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class file_open_kind_expression(parser.expression):

    def __init__(self, sString):
        parser.expression.__init__(self, sString)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class file_logical_name(parser.expression):

    def __init__(self, sString):
        parser.expression.__init__(self, sString)

