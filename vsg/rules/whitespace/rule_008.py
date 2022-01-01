
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import whitespace


class rule_008(whitespace.Rule):
    '''
    This rule checks for spaces after the **std_logic_vector** keyword.

    **Violation**

    .. code-block:: vhdl

       signal data    : std_logic_vector (7 downto 0);
       signal counter : std_logic_vector    (7 downto 0);

    **Fix**

    .. code-block:: vhdl

       signal data    : std_logic_vector(7 downto 0);
       signal counter : std_logic_vector(7 downto 0);
    '''

    def __init__(self):
        whitespace.Rule.__init__(self, 'whitespace', '008')
        self.solution = 'Remove spaces after std_logic_vector'

    def _get_tokens_of_interest(self, oFile):
        return [oFile.get_all_tokens()]

    def _analyze(self, lToi):
        oToi = lToi[0]
        iLine, lTokens = utils.get_toi_parameters(oToi)
        for iToken, oToken in enumerate(lTokens[:len(lTokens) - 2]):

            iLine = utils.increment_line_number(iLine, oToken)

            if oToken.get_value().lower() == 'std_logic_vector':
                if utils.are_next_consecutive_token_types([parser.whitespace, parser.open_parenthesis], iToken + 1, lTokens):
                    lExtractedTokens = oToi.extract_tokens(iToken, iToken + 1)
                    oViolation = violation.New(iLine, lExtractedTokens, self.solution)
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lTokens.pop()
        oViolation.set_tokens(lTokens)
