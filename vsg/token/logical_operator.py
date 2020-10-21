
from vsg import parser


class logical_operator(parser.keyword):

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class and_operator(logical_operator):

    def __init__(self, sString):
        logical_operator.__init__(self, sString)


class or_operator(logical_operator):

    def __init__(self, sString):
        logical_operator.__init__(self, sString)


class nand_operator(logical_operator):

    def __init__(self, sString):
        logical_operator.__init__(self, sString)


class nor_operator(logical_operator):

    def __init__(self, sString):
        logical_operator.__init__(self, sString)


class xor_operator(logical_operator):

    def __init__(self, sString):
        logical_operator.__init__(self, sString)


class xnor_operator(logical_operator):

    def __init__(self, sString):
        logical_operator.__init__(self, sString)
