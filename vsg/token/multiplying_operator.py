
from vsg import parser


class multiplying_operator(parser.keyword):
    '''
    unique_id = multiplying_operator : multiplying_operator
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class star(multiplying_operator):
    '''
    unique_id = multiplying_operator : star
    '''

    def __init__(self, sString='*'):
        multiplying_operator.__init__(self, '*')


class slash(multiplying_operator):
    '''
    unique_id = multiplying_operator : slash
    '''

    def __init__(self, sString='/'):
        multiplying_operator.__init__(self, '/')


class mod_operator(multiplying_operator):
    '''
    unique_id = multiplying_operator : mod_operator
    '''

    def __init__(self, sString):
        multiplying_operator.__init__(self, sString)


class rem_operator(multiplying_operator):
    '''
    unique_id = multiplying_operator : rem_operator
    '''

    def __init__(self, sString):
        multiplying_operator.__init__(self, sString)
