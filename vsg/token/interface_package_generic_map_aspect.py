
from vsg import parser


class generic_keyword(parser.keyword):
    '''
    unique_id = interface_package_generic_map_aspect : generic_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class map_keyword(parser.keyword):
    '''
    unique_id = interface_package_generic_map_aspect : map_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = interface_package_generic_map_aspect : open_parenthesis
    '''

    def __init__(self, sString='('):
        parser.open_parenthesis.__init__(self)


class default_keyword(parser.keyword):
    '''
    unique_id = interface_package_generic_map_aspect : default_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class undefined_range(parser.undefined_range):
    '''
    unique_id = interface_package_generic_map_aspect : undefined_range
    '''

    def __init__(self, sString='<>'):
        parser.undefined_range.__init__(self)


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = interface_package_generic_map_aspect : close_parenthesis
    '''

    def __init__(self, sString=')'):
        parser.close_parenthesis.__init__(self)
