from vsg import parser


class if_label(parser.label):
    '''
    unique_id = if_statement : if_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class label_colon(parser.label_colon):
    '''
    unique_id = if_statement : label_colon
    '''

    def __init__(self):
        parser.label_colon.__init__(self)


class if_keyword(parser.keyword):
    '''
    unique_id = if_statement : if_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class then_keyword(parser.keyword):
    '''
    unique_id = if_statement : then_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class elsif_keyword(parser.keyword):
    '''
    unique_id = if_statement : elsif_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class else_keyword(parser.keyword):
    '''
    unique_id = if_statement : else_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_keyword(parser.keyword):
    '''
    unique_id = if_statement : end_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_if_keyword(parser.keyword):
    '''
    unique_id = if_statement : end_if_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class end_if_label(parser.label):
    '''
    unique_id = if_statement : end_if_label
    '''

    def __init__(self, sString):
        parser.label.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = if_statement : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
