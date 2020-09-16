
from vsg import parser


class block_label(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):

    def __init__(self, sString=':'):
        parser.label_colon.__init__(self)


class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class guard_open_parenthesis(parser.open_parenthesis):

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class guard_condition(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class guard_close_parenthesis(parser.close_parenthesis):

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_block_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_block_label(parser.label):

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
