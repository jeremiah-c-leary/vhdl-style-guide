
from vsg import parser


class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class pure_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class impure_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class designator(parser.designator):

    def __init__(self, sString):
        parser.designator.__init__(self, sString)

class parameter_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class open_parenthesis(parser.open_parenthesis):

    def __init__(self):
        parser.open_parenthesis.__init__(self)

class close_parenthesis(parser.close_parenthesis):

    def __init__(self):
        parser.open_parenthesis.__init__(self)

class return_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class type_mark(parser.type_mark):

    def __init__(self, sString):
        parser.type_mark.__init__(self, sString)

