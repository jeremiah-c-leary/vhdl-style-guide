
from vsg import parser


class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class condition(parser.condition):

    def __init__(self, sString):
        parser.condition.__init__(self, sString)


class report_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class report_expression(parser.expression):

    def __init__(self, sString):
        parser.expression.__init__(self, sString)


class severity_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class severity_expression(parser.expression):

    def __init__(self, sString):
        parser.expression.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)


