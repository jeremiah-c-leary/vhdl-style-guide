
from vsg import violation

from vsg.token import port_clause as token
from vsg.token import mode
from vsg.rule_group import structure


class rule_023(structure.Rule):
    '''
    This rule checks for missing modes in port declarations.

    .. NOTE:: This must be fixed by the user.  VSG makes no assumption on the direction of the port.

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : std_logic;
         RD_EN    : std_logic;
         OVERFLOW : std_logic;
         DATA     : inout std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic
       );
    '''

    def __init__(self):
        structure.Rule.__init__(self, name='port', identifier='023')
        self.solution = 'Add mode'
        self.fixable = False

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_interface_elements_between_tokens(token.open_parenthesis, token.close_parenthesis)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for oToken in lTokens:
                if isinstance(oToken, mode.mode):
                    break
            else:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        '''
        Applies fixes for any rule violations.
        '''
        return None
