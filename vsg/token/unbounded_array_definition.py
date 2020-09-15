
from vsg import parser


class array_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class comma(parser.comma):

    def __init__(self, sString=','):
        parser.comma.__init__(self)


class close_parenthesis(parser.close_parenthesis):

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class of_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

# jcl - remove objects below after new parser is done


class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class index_subtype_definition(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class subtype_indication(parser.subtype_indication):

    def __init__(self):
        parser.subtype_indication.__init__(self)
