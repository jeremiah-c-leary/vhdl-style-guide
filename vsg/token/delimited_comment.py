
from vsg import parser


class beginning(parser.comment):
    '''
    unique_id = delimited_comment : beginning
    '''

    def __init__(self, sString='/*'):
        parser.comment.__init__(self, sString)


class ending(parser.comment):
    '''
    unique_id = delimited_comment : ending
    '''

    def __init__(self, sString='*/'):
        parser.comment.__init__(self, sString)


class text(parser.item):
    '''
    unique_id = delimited_comment : text
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)
