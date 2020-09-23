

from vsg import parser
from vsg import rule_item
from vsg import violation


class insert_token_right_of_token_if_it_does_not_exist(rule_item.Rule):
    '''
    Checks for the existence of a token and will insert it if it does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    insert_token : token object
       token to insert if it does not exist.

    anchor_token : token object
       token to check if insert_token exists to the right of
    '''

    def __init__(self, name, identifier, insert_token, anchor_token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.insert_token = insert_token
        self.anchor_token = anchor_token

    def analyze(self, oFile):
        lToi = oFile.get_sequence_of_tokens_not_matching([self.anchor_token, parser.whitespace, type(self.insert_token)])
        for oToi in lToi:
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
            lTokens.append(parser.whitespace(' '))
            lTokens.append(self.insert_token)
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
