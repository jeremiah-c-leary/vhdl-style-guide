
from vsg import parser


class component_keyword(parser.keyword):
    '''
    unique_id = instantiated_unit : component_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class component_name(parser.name):
    '''
    unique_id = instantiated_unit : component_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class entity_keyword(parser.keyword):
    '''
    unique_id = instantiated_unit : entity_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class entity_name(parser.name):
    '''
    unique_id = instantiated_unit : entity_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = instantiated_unit : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class architecture_identifier(parser.identifier):
    '''
    unique_id = instantiated_unit : architecture_identifier
    '''

    def __init__(self, sString):
        parser.identifier.__init__(self, sString)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = instantiated_unit : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)


class configuration_keyword(parser.keyword):
    '''
    unique_id = instantiated_unit : configuration_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class configuration_name(parser.name):
    '''
    unique_id = instantiated_unit : configuration_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)

