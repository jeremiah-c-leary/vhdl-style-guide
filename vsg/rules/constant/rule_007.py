
from vsg import violation

from vsg.token import constant_declaration as token
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class rule_007(structure.Rule):
    '''
    This rule checks the **:=** is on the same line at the **constant** keyword.

    **Violation**

    .. code-block:: vhdl

       constant size : integer
          := 1;

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;

    **Fix**

    .. code-block:: vhdl

       constant size    : integer := 1;
       constant width   : integer := 32
    '''

    def __init__(self):
        structure.Rule.__init__(self, 'constant', '007')
        self.solution = 'move assignment to same line as constant declaration.'
        self.fixable = False  # Too complicated at the moment to fix.

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by_tokens_if_token_is_between_them(token.constant_keyword, token.semicolon, token.assignment_operator)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            for oToken in lTokens:
                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, token.constant_keyword):
                    iKeywordLine = iLine

                if isinstance(oToken, token.assignment_operator):
                    if iKeywordLine != iLine:
                        oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                        self.add_violation(oViolation)
