
from vsg import parser
from vsg import violation

from vsg.rule_group.blank_line import Rule
from vsg.rules import utils


class rule_200(Rule):
    '''
    This rule removes consecutive blank lines.

    **Violation**

    .. code-block:: vhdl

       a <= b;


       c <= d;

    **Fix**

    .. code-block:: vhdl

       a <= b;

       c <= d;
    '''

    def __init__(self):
        Rule.__init__(self, name='whitespace', identifier='200')
        self.blank_lines_allowed = 1
        self.configuration.append('blank_lines_allowed')

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_consecutive_lines_starting_with_token(parser.blank_line)
        lReturn = []
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) > ((self.blank_lines_allowed * 2) - 1):
                lReturn.append(oToi)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iBlankLines = utils.number_of_tokens_in_token_list(parser.blank_line, lTokens)

            if iBlankLines > self.blank_lines_allowed:
                sSolution = f'Remove {iBlankLines - self.blank_lines_allowed}'
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                dAction = {}
                dAction['remove_index'] = len(lTokens) - (iBlankLines - self.blank_lines_allowed) * 2
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lNewTokens = lTokens[0:dAction['remove_index']]
        oViolation.set_tokens(lNewTokens)
