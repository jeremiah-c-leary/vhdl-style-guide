

from vsg import parser
from vsg import rule_item
from vsg import violation


class single_space_between_tokens(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    left_token : token object
       The left token to check for a space between the right token

    right_token : token object
       The right token to check for a space between the left token
    '''

    def __init__(self, name, identifier, left_token, right_token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.left_token = left_token
        self.right_token = right_token

    def analyze(self, oFile):
        lToi = oFile.get_sequence_of_tokens_matching([self.left_token, parser.whitespace, self.right_token])
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens[1].get_value()) != 1:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            lTokens[1].set_value(' ')
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
