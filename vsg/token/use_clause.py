
from vsg import parser

###############################################################################
# Use objects
###############################################################################


class keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)

class selected_name(parser.selected_name):

    def __init__(self, sString):
        parser.selected_name.__init__(self, sString)

class comma(parser.comma):

    def __init__(self):
        parser.comma.__init__(self)

class semicolon(parser.semicolon):

    def __init__(self):
        parser.semicolon.__init__(self)
