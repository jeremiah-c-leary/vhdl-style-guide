
from vsg import parser


class shared_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class variable_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)

class comma(parser.comma):

    def __init__(self):
        parser.comma.__init__(self)

class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)

class subtype_indication(parser.subtype_indication):

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)

class assignment_operator(parser.item):

    def __init__(self, sString=':='):
        parser.item.__init__(self, sString)

class assignment_expression(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)

class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
