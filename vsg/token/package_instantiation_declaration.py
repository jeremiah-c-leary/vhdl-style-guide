
from vsg import parser


class package_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class is_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class new_keyword(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class uninstantiated_package_name(parser.name):

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class semicolon(parser.semicolon):

    def __init__(self, sString):
        parser.semicolon.__init__(self)
