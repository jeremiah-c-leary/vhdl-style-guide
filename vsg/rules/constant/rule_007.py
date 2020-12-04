
from vsg import rule
from vsg import violation

from vsg.token import constant_declaration as token

from vsg.vhdlFile import utils


class rule_007(rule.Rule):
    '''
    Checks the assignment operator is on the same line as the constant keyword.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'constant', '007')
        self.solution = 'move assignment to same line as constant declaration.'
        self.phase = 1
        self.fixable = False  # Too complicated at the moment to fix.

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by_tokens_if_token_is_between_them(token.constant_keyword, token.semicolon, token.assignment_operator)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if utils.find_carriage_return(lTokens) is not None:
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                self.add_violation(oViolation)
