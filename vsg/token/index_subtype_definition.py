from vsg import parser


class range_keyword(parser.keyword):
    '''
    unique_id = index_subtype_definition : range_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class undefined_range(parser.undefined_range):
    '''
    unique_id = index_subtype_definition : undefined_range
    '''

    def __init__(self, sString='<>'):
        parser.undefined_range.__init__(self)
