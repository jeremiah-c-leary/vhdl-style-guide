
from vsg import parser

###############################################################################
# Entity objects
###############################################################################

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class open_parenthesis(parser.open_parenthesis):

    def __init__(self,):
        parser.open_parenthesis.__init__(self)

class index_subtype_definition(parser.item):

    def __init__(self, sString):
        parser.item.__init__(self, sString)

class comma(parser.comma):

    def __init__(self,):
        parser.comma.__init__(self)

class close_parenthesis(parser.close_parenthesis):

    def __init__(self,):
        parser.close_parenthesis.__init__(self)

class of_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class subtype_indication(parser.subtype_indication):

    def __init__(self):
        parser.subtype_indication.__init__(self)
