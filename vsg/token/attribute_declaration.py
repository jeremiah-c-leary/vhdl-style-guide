
from vsg import parser


class attribute_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class colon(parser.colon):

    def __init__(self, sString=':'):
        parser.colon.__init__(self)


class semicolon(parser.semicolon):

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)

# jcl - remove the following objects after the new parser is done

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)



class type_mark(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


