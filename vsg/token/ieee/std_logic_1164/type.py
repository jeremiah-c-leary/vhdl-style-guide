
from vsg import parser


class std_logic_vector(parser.type):

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class std_ulogic_vector(parser.type):

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class std_ulogic(parser.type):

    def __init__(self, sString):
        parser.type.__init__(self, sString)
