
from vsg import parser


class operator(parser.keyword):
    '''
    unique_id = adding_operator : operator
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class plus(operator):
    '''
    unique_id = adding_operator : plus
    '''

    def __init__(self, sString='+'):
        operator.__init__(self, '+')


class minus(operator):
    '''
    unique_id = adding_operator : minus
    '''

    def __init__(self, sString='-'):
        operator.__init__(self, '-')


class concat(operator):
    '''
    unique_id = adding_operator : concat
    '''

    def __init__(self, sString='&'):
        operator.__init__(self, '&')
