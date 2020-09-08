
from vsg import parser


class constant_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)

class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)

class assignment_operator(parser.item):

    def __init__(self, sString=':='):
        parser.item.__init__(self, ':=')

# jcl - remove object below when new parser is done

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)

class comma(parser.comma):

    def __init__(self):
        parser.comma.__init__(self)

class subtype_indication(parser.subtype_indication):

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)

class assignment_expression(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)

