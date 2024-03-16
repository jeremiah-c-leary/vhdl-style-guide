
from vsg import parser

###############################################################################
# Inteface List objects
###############################################################################


class semicolon(parser.semicolon):
    '''
    unique_id = interface_list : semicolon
    '''

    def __init__(self, sString=';'):
        super().__init__()
