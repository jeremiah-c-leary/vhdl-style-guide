# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import whitespace
from vsg.vhdlFile import utils


class rule_008(whitespace.Rule):
    """
    This rule checks for spaces after the **std_logic_vector** keyword.

    **Violation**

    .. code-block:: vhdl

       signal data    : std_logic_vector (7 downto 0);
       signal counter : std_logic_vector    (7 downto 0);

    **Fix**

    .. code-block:: vhdl

       signal data    : std_logic_vector(7 downto 0);
       signal counter : std_logic_vector(7 downto 0);
    """

    def __init__(self):
        super().__init__()
        self.solution = "Remove spaces after std_logic_vector"
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        return [oFile.get_all_tokens()]

    def _analyze(self, lToi):
        oToi = lToi[0]
        iLine, lTokens = utils.get_toi_parameters(oToi)
        for iToken, oToken in enumerate(lTokens[: len(lTokens) - 2]):
            iLine = utils.increment_line_number(iLine, oToken)

            if oToken.get_lower_value() == "std_logic_vector":
                if utils.are_next_consecutive_token_types([parser.whitespace, parser.open_parenthesis], iToken + 1, lTokens):
                    lExtractedTokens = oToi.extract_tokens(iToken, iToken + 1)
                    oViolation = violation.New(iLine, lExtractedTokens, self.solution)
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lTokens.pop()
        oViolation.set_tokens(lTokens)
