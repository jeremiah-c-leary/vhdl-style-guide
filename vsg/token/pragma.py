
from vsg import parser


class ignore(parser.item):
    '''
    unique_id = pragma : ignore
    '''

    def __init__(self, sString):
        parser.item.__init__(self, sString)


class pragma(parser.comment):
    '''
    unique_id = pragma : pragma
    '''

    def __init__(self, sString):
        parser.comment.__init__(self, sString)


class open(pragma):
    '''
    unique_id = pragma : open
    '''

    def __init__(self, sString):
        pragma.__init__(self, sString)


class close(pragma):
    '''
    unique_id = pragma : close
    '''

    def __init__(self, sString):
        pragma.__init__(self, sString)


class single(pragma):
    '''
    unique_id = pragma : single
    '''

    def __init__(self, sString):
        pragma.__init__(self, sString)

