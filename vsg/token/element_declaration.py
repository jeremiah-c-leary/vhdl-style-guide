
from vsg import parser


class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)

# jcl - remove the folling objects when the new parser is done

class identifier(parser.identifier):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class comma(parser.comma):

    def __init__(self):
        parser.comma.__init__(self)

class element_subtype_definition(parser.subtype_definition):

    def __init__(self, sString):
        parser.subtype_definition.__init__(self, sString)
