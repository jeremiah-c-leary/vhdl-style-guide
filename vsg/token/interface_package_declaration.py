
from vsg import parser


class package_keyword(parser.keyword):
    '''
    unique_id = interface_package_declaration : package_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class is_keyword(parser.keyword):
    '''
    unique_id = interface_package_declaration : is_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class new_keyword(parser.keyword):
    '''
    unique_id = interface_package_declaration : new_keyword
    '''

    def __init__(self, sString):
        parser.keyword.__init__(self, sString)


class uninstantiated_package_name(parser.name):
    '''
    unique_id = interface_package_declaration : uninstantiated_package_name
    '''

    def __init__(self, sString):
        parser.name.__init__(self, sString)
