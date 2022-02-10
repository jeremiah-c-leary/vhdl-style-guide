
from vsg import parser


class std_logic_vector(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : std_logic_vector
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class std_ulogic_vector(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : std_ulogic_vector
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class std_ulogic(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : std_ulogic
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class std_logic(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : std_logic
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class integer(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : integer
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class signed(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : signed
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class unsigned(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : unsigned
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)


class natural(parser.type):
    '''
    unique_id = ieee_std_logic_1164_types : natural
    '''

    def __init__(self, sString):
        parser.type.__init__(self, sString)
