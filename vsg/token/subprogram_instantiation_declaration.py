from vsg import parser


class identifier(parser.identifier):
    '''
    unique_id = subprogram_instantiation_declaration : identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = subprogram_instantiation_declaration : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class new_keyword(parser.keyword):
    '''
    unique_id = subprogram_instantiation_declaration : new_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class uninstantiated_subprogram_name(parser.name):
    '''
    unique_id = subprogram_instantiation_declaration : uninstantiated_subprogram_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = subprogram_instantiation_declaration : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)
