
from vsg import parser


class e_keyword(parser.keyword):
    '''
    unique_id = exponent : e_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class plus_sign(parser.item):
    '''
    unique_id = exponent : plus_sign
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class minus_sign(parser.item):
    '''
    unique_id = exponent : minus_sign
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class integer(parser.integer):
    '''
    unique_id = exponent : integer
    '''

    def __init__(self, sString):
        parser.integer.__init__(self, sString)
