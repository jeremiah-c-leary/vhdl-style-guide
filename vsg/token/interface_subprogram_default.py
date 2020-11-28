from vsg import parser


class subprogram_name(parser.name):
    '''
    unique_id = interface_subprogram_default : subprogram_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class undefined_range(parser.undefined_range):
    '''
    unique_id = interface_subprogram_default : undefined_range
    '''

    def __init__(self, sString='<>'):
        parser.undefined_range.__init__(self)
