from vsg import parser


class procedure_keyword(parser.keyword):
    '''
    unique_id = subprogram_kind : procedure_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class function_keyword(parser.keyword):
    '''
    unique_id = subprogram_kind : function_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)
