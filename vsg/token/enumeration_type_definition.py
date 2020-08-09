
from vsg import parser

###############################################################################
# Entity objects
###############################################################################

class open_parenthesis(parser.open_parenthesis):

    def __init__(self):
        parser.open_parenthesis.__init__(self)


class enumeration_literal(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class comma(parser.comma):

    def __init__(self):
        parser.comma.__init__(self)


class close_parenthesis(parser.close_parenthesis):

    def __init__(self):
        parser.close_parenthesis.__init__(self)

