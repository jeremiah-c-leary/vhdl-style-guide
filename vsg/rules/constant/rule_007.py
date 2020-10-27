
from vsg import rule_item
from vsg import parser
from vsg import violation

from vsg.token import constant_declaration as token

from vsg.vhdlFile import utils


class rule_007(rule_item.Rule):
    '''
    Checks the assignment operator is on the same line as the constant keyword.
    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'constant', '007')
        self.solution = 'move assignment to same line as constant declaration.'
        self.phase = 1
        self.fixable = False  # Too complicated at the moment to fix.

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(token.constant_keyword, token.assignment_operator)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if utils.find_carriage_return(0, lTokens) is not None:
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                self.add_violation(oViolation)


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        return
