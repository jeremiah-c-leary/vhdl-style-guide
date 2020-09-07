
from vsg import parser


class subtype_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)

# jcl - remove the following objects when the new parser is done

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)

class subtype_indication(parser.subtype_indication):

    def __init__(self, sString):
        parser.subtype_indication.__init__(self, sString)

