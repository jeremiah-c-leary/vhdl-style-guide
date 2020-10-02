

from vsg import parser
from vsg import rule_item
from vsg import violation


class insert_token_right_of_token_if_it_does_not_exist_before_token(rule_item.Rule):
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

    anchor_token : token object type
       token to check if insert_token exists to the right of

    end_token : token object type
       token that bounds the search for the insert_token
    '''

    def __init__(self, name, identifier, insert_token, anchor_token, end_token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.end_token = end_token

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.anchor_token, self.end_token)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bFound = False
            for oToken in lTokens:
                if isinstance(oToken, type(self.insert_token)):
                    bFound = True
                    break
            if not bFound:
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
            lTokens.insert(1, self.insert_token)
            lTokens.insert(1, parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
