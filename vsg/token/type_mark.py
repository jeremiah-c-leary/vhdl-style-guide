from vsg import parser


class name(parser.name):
    '''
    unique_id = type_mark : name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)
