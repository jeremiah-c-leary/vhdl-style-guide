
from vsg.rules import move_token as Rule

from vsg import token

oToken = token.port_map_aspect.close_parenthesis


class rule_004(Rule):
    '''
    This rule checks the location of the closing ")" character for the port map.

    The default location is on a line by itself.

    Refer to the section `Configuring Closing Parenthesis Location<configuring-closing-parenthesis-location>`_ for information on options.

    **Violation**

    .. code-block:: vhdl

        port map (
          WR_EN => wr_en);

    **Fix**

    .. code-block:: vhdl

        port map (
          WR_EN => wr_en
        );
    '''

    def __init__(self):
        Rule.__init__(self, 'port_map', '004', oToken)
