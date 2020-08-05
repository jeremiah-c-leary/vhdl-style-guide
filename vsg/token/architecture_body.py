from vsg import parser

###############################################################################
# Architecture objects
###############################################################################

class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class identifier(parser.identifier):

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)

class of_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class entity_name(parser.name):

    def __init__(self, sString):
        parser.name.__init__(self, sString)

class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class begin_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class end_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class end_architecture_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class simple_name(parser.simple_name):

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)

class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
