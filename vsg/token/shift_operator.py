
from vsg import parser


class shift_operator(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class sll(shift_operator):

    def __init__(self, sString):
        shift_operator.__init__(self, sString)


class srl(shift_operator):

    def __init__(self, sString):
        shift_operator.__init__(self, sString)


class sla(shift_operator):

    def __init__(self, sString):
        shift_operator.__init__(self, sString)


class sra(shift_operator):

    def __init__(self, sString):
        shift_operator.__init__(self, sString)


class rol(shift_operator):

    def __init__(self, sString):
        shift_operator.__init__(self, sString)


class ror(shift_operator):

    def __init__(self, sString):
        shift_operator.__init__(self, sString)
