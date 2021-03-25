
from vsg import parser


class unary_logical_operator(parser.keyword):
    '''
    unique_id = unary_logical_operator : unary_logical_operator
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class and_operator(unary_logical_operator):
    '''
    unique_id = unary_logical_operator : and_operator
    '''

    def __init__(self, sString):
        unary_logical_operator.__init__(self, sString)


class or_operator(unary_logical_operator):
    '''
    unique_id = unary_logical_operator : or_operator
    '''

    def __init__(self, sString):
        unary_logical_operator.__init__(self, sString)


class nand_operator(unary_logical_operator):
    '''
    unique_id = unary_logical_operator : nand_operator
    '''

    def __init__(self, sString):
        unary_logical_operator.__init__(self, sString)


class nor_operator(unary_logical_operator):
    '''
    unique_id = unary_logical_operator : nor_operator
    '''

    def __init__(self, sString):
        unary_logical_operator.__init__(self, sString)


class xor_operator(unary_logical_operator):
    '''
    unique_id = unary_logical_operator : xor_operator
    '''

    def __init__(self, sString):
        unary_logical_operator.__init__(self, sString)


class xnor_operator(unary_logical_operator):
    '''
    unique_id = unary_logical_operator : xnor_operator
    '''

    def __init__(self, sString):
        unary_logical_operator.__init__(self, sString)
