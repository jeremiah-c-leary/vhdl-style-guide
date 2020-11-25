
from vsg import parser


class mode(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class in_keyword(mode):

    def __init__(self, sString):
        mode.__init__(self, sString)


class out_keyword(mode):

    def __init__(self, sString):
        mode.__init__(self, sString)


class inout_keyword(mode):

    def __init__(self, sString):
        mode.__init__(self, sString)


class buffer_keyword(mode):

    def __init__(self, sString):
        mode.__init__(self, sString)


class linkage_keyword(mode):

    def __init__(self, sString):
        mode.__init__(self, sString)
