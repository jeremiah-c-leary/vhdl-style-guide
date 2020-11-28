
from vsg import parser


class sign(parser.keyword):
    '''
    unique_id = sign : sign
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class plus(sign):
    '''
    unique_id = sign : plus
    '''

    def __init__(self, sString='+'):
        sign.__init__(self, '+')


class minus(sign):
    '''
    unique_id = sign : minus
    '''

    def __init__(self, sString='-'):
        sign.__init__(self, '-')
