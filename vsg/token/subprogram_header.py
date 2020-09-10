
from vsg import parser


class generic_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class close_parenthesis(parser.close_parenthesis):

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)

# jcl - remove object below after new parser is done

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

