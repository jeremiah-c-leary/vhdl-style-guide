from vsg import parser


class is_keyword(parser.keyword):
    '''
    unique_id = subprogram_body : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class begin_keyword(parser.keyword):
    '''
    unique_id = subprogram_body : begin_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = subprogram_body : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class designator(parser.designator):
    '''
    unique_id = subprogram_body : designator
    '''

    def __init__(self, sString):
        parser.designator.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = subprogram_body : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
