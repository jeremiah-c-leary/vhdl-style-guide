from vsg import parser


class name(parser.name):
    '''
    unique_id = type_mark : name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class tic(parser.tic):
    '''
    unique_id = type_mark : tic
    '''

    def __init__(self, sString):
        parser.tic.__init__(self, sString)


class attribute(parser.attribute):
    '''
    unique_id = type_mark : attribute
    '''

    def __init__(self, sString):
        parser.attribute.__init__(self, sString)

