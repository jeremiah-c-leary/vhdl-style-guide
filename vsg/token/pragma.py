
from vsg import parser


class ignore(parser.item):
    '''
    unique_id = pragma : ignore
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class pragma(parser.item):
    '''
    unique_id = pragma : pragma
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)
